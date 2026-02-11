import os
from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from azure.core.exceptions import HttpResponseError
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient

# ---------------- LOAD ENV (LOCAL ONLY) ----------------
# In Azure App Service, env comes from Configuration -> Application settings
if not os.getenv("WEBSITE_SITE_NAME"):
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except Exception:
        pass

# ---------------- FLASK APP ----------------
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "secret123")

# ---------------- HEALTH CHECK (IMPORTANT FOR AZURE) ----------------
@app.route("/healthz")
def healthz():
    return "ok", 200

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
    raise RuntimeError("Missing Azure env vars in App Service: " + ", ".join(missing))

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
@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == "admin@gmail.com" and password == "admin123":
            session["user"] = email
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if not require_login():
        return redirect(url_for("login"))
    return render_template("dashboard.html")

# ---------------- STEP 7: RESOURCE GROUP APIs ----------------
@app.route("/api/resource-groups")
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

@app.route("/api/resources")
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
@app.route("/api/vms")
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

# (keep your other VM endpoints same: details/start/stop/restart/delete/status-count)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
