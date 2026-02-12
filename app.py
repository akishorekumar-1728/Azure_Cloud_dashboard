import os
from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from azure.core.exceptions import HttpResponseError
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient

# ---------------- LOAD ENV (LOCAL ONLY) ----------------
if not os.getenv("WEBSITE_SITE_NAME"):
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except Exception:
        pass

# ---------------- FLASK APP ----------------
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "secret123")

# ---------------- HEALTH CHECK (NO LOGIN REQUIRED) ----------------
@app.get("/healthz")
def healthz():
    return jsonify({"status": "ok"}), 200

# ---------------- ADMIN LOGIN (FROM ENV) ----------------
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@gmail.com")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

# ---------------- AZURE AUTH ----------------
TENANT_ID = os.getenv("AZURE_TENANT_ID")
CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID")

missing = [k for k, v in {
    "AZURE_TENANT_ID": TENANT_ID,
    "AZURE_CLIENT_ID": CLIENT_ID,
    "AZURE_CLIENT_SECRET": CLIENT_SECRET,
    "AZURE_SUBSCRIPTION_ID": SUBSCRIPTION_ID,
}.items() if not v]

if missing:
    raise RuntimeError("Missing Azure env vars: " + ", ".join(missing))

credential = ClientSecretCredential(
    tenant_id=TENANT_ID,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

compute_client = ComputeManagementClient(credential, SUBSCRIPTION_ID)
resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)

# ---------------- HELPERS ----------------
def extract_rg_from_id(resource_id: str) -> str:
    try:
        return resource_id.split("/")[4]
    except Exception:
        return ""

def get_power_state(resource_group: str, vm_name: str) -> str:
    instance = compute_client.virtual_machines.instance_view(resource_group, vm_name)
    for s in instance.statuses:
        if s.code and s.code.startswith("PowerState/"):
            return s.code.split("/")[-1].lower()
    return "unknown"

def require_login() -> bool:
    return "user" in session

# ---------------- ROUTES ----------------
@app.get("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip()
        password = (request.form.get("password") or "").strip()

        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session["user"] = email
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.get("/dashboard")
def dashboard():
    if not require_login():
        return redirect(url_for("login"))
    return render_template("dashboard.html")

# ---------------- RESOURCE GROUP APIs ----------------
@app.get("/api/resource-groups")
def list_resource_groups():
    if not require_login():
        return jsonify({"error": "Unauthorized"}), 401
    try:
        rgs = [{"name": rg.name, "location": rg.location} for rg in resource_client.resource_groups.list()]
        rgs.sort(key=lambda x: (x["name"] or "").lower())
        return jsonify(rgs), 200
    except HttpResponseError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@app.get("/api/resources")
def list_resources_in_rg():
    if not require_login():
        return jsonify({"error": "Unauthorized"}), 401
    try:
        rg_name = request.args.get("rg")
        if not rg_name:
            return jsonify({"error": "rg is required"}), 400

        items = []
        for res in resource_client.resources.list_by_resource_group(rg_name):
            items.append({"name": res.name, "type": res.type, "location": res.location})

        items.sort(key=lambda x: ((x["type"] or "").lower(), (x["name"] or "").lower()))
        return jsonify(items), 200
    except HttpResponseError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

# ---------------- VM APIs ----------------
@app.get("/api/vms")
def list_vms():
    if not require_login():
        return jsonify({"error": "Unauthorized"}), 401
    try:
        vm_list = []
        for vm in compute_client.virtual_machines.list_all():
            rg = extract_rg_from_id(vm.id)
            status = get_power_state(rg, vm.name) if rg else "unknown"
            vm_list.append({
                "name": vm.name,
                "resource_group": rg,
                "status": status,
                "location": getattr(vm, "location", None)
            })
        return jsonify(vm_list), 200
    except HttpResponseError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@app.post("/api/vm/start")
def start_vm():
    if not require_login():
        return jsonify({"error": "Unauthorized"}), 401
    try:
        data = request.json or {}
        rg = data.get("resource_group")
        vm_name = data.get("vm_name")
        if not rg or not vm_name:
            return jsonify({"error": "resource_group and vm_name are required"}), 400
        compute_client.virtual_machines.begin_start(rg, vm_name)
        return jsonify({"message": "VM start initiated"}), 200
    except HttpResponseError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@app.post("/api/vm/stop")
def stop_vm():
    if not require_login():
        return jsonify({"error": "Unauthorized"}), 401
    try:
        data = request.json or {}
        rg = data.get("resource_group")
        vm_name = data.get("vm_name")
        if not rg or not vm_name:
            return jsonify({"error": "resource_group and vm_name are required"}), 400
        compute_client.virtual_machines.begin_deallocate(rg, vm_name)
        return jsonify({"message": "VM stop initiated"}), 200
    except HttpResponseError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@app.post("/api/vm/restart")
def restart_vm():
    if not require_login():
        return jsonify({"error": "Unauthorized"}), 401
    try:
        data = request.json or {}
        rg = data.get("resource_group")
        vm_name = data.get("vm_name")
        if not rg or not vm_name:
            return jsonify({"error": "resource_group and vm_name are required"}), 400
        compute_client.virtual_machines.begin_restart(rg, vm_name)
        return jsonify({"message": "VM restart initiated"}), 200
    except HttpResponseError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@app.post("/api/vm/delete")
def delete_vm():
    if not require_login():
        return jsonify({"error": "Unauthorized"}), 401
    try:
        data = request.json or {}
        rg = data.get("resource_group")
        vm_name = data.get("vm_name")
        if not rg or not vm_name:
            return jsonify({"error": "resource_group and vm_name are required"}), 400
        compute_client.virtual_machines.begin_delete(rg, vm_name)
        return jsonify({"message": "VM delete initiated"}), 200
    except HttpResponseError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@app.get("/api/vm/status-count")
def vm_status_count():
    if not require_login():
        return jsonify({"error": "Unauthorized"}), 401
    try:
        total = running = stopped = other = 0
        for vm in compute_client.virtual_machines.list_all():
            total += 1
            rg = extract_rg_from_id(vm.id)
            state = get_power_state(rg, vm.name) if rg else "unknown"
            if state == "running":
                running += 1
            elif state in ("stopped", "deallocated"):
                stopped += 1
            else:
                other += 1

        return jsonify({
            "total": total,
            "running": running,
            "stopped": stopped,
            "other": other
        }), 200
    except HttpResponseError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
@app.get("/api/vm/details")
def vm_details():
    if not require_login():
        return jsonify({"error": "Unauthorized"}), 401
    try:
        rg = request.args.get("resource_group")
        vm_name = request.args.get("vm_name")
        if not rg or not vm_name:
            return jsonify({"error": "resource_group and vm_name are required"}), 400

        vm = compute_client.virtual_machines.get(rg, vm_name)
        power_state = get_power_state(rg, vm_name)

        vm_size = vm.hardware_profile.vm_size if vm.hardware_profile else None

        os_type = None
        if vm.storage_profile and vm.storage_profile.os_disk and vm.storage_profile.os_disk.os_type:
            raw = vm.storage_profile.os_disk.os_type
            os_type = raw.value if hasattr(raw, "value") else str(raw)

        return jsonify({
            "name": vm.name,
            "resource_group": rg,
            "location": vm.location,
            "vm_size": vm_size,
            "os_type": os_type,
            "power_state": power_state
        }), 200

    except HttpResponseError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

# ---------------- LOCAL / VM RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
