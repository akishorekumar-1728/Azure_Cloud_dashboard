from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from dotenv import load_dotenv
import os

from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient

# Load environment variables
load_dotenv()

# Flask app
app = Flask(__name__)
app.secret_key = "secret123"

# ---------------- AZURE AUTH ----------------

credential = ClientSecretCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    client_id=os.getenv("AZURE_CLIENT_ID"),
    client_secret=os.getenv("AZURE_CLIENT_SECRET")
)

subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
compute_client = ComputeManagementClient(credential, subscription_id)

# ---------------- AUTH ROUTES ----------------

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == "admin@gmail.com" and password == "admin123":
            session["user"] = email
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")



@app.route('/logout')
def logout():
    session.clear()   # 🔥 clears full session
    return redirect(url_for('login'))


# ---------------- DASHBOARD ----------------

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template('dashboard.html')



# ---------------- API ROUTES ----------------

@app.route("/api/vms")
def list_vms():
    vm_list = []

    for vm in compute_client.virtual_machines.list_all():
        rg = vm.id.split("/")[4]
        instance = compute_client.virtual_machines.instance_view(rg, vm.name)
        status = "stopped"

        for s in instance.statuses:
            if s.code.startswith("PowerState/"):
                status = s.code.split("/")[-1].lower()

        vm_list.append({
            "name": vm.name,
            "resource_group": rg,
            "status": status
        })

    return jsonify(vm_list)


@app.route("/api/vm/start", methods=["POST"])
def start_vm():
    data = request.json
    compute_client.virtual_machines.begin_start(
        data["resource_group"],
        data["vm_name"]
    )
    return jsonify({"message": "VM starting"})


@app.route("/api/vm/stop", methods=["POST"])
def stop_vm():
    data = request.json
    compute_client.virtual_machines.begin_deallocate(
        data["resource_group"],
        data["vm_name"]
    )
    return jsonify({"message": "VM stopping"})


@app.route("/api/vm/status-count")
def vm_status_count():
    running = 0
    stopped = 0
    total = 0

    for vm in compute_client.virtual_machines.list_all():
        total += 1
        rg = vm.id.split("/")[4]
        instance = compute_client.virtual_machines.instance_view(rg, vm.name)

        for s in instance.statuses:
            if s.code.lower() == "powerstate/running":
                running += 1
            elif s.code.lower() == "powerstate/deallocated":
                stopped += 1

    return jsonify({
        "running": running,
        "stopped": stopped,
        "total": total
    })



# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
