

# 🚀 Azure Cloud Dashboard

## 📌 Project Statement

Azure Cloud Dashboard is a web-based cloud management application that enables users to monitor and manage Microsoft Azure Virtual Machines and Resource Groups through a centralized dashboard. The system securely connects to Azure using Service Principal authentication and provides real-time resource monitoring and control.

---
 
## ✨ Features

### 🔹 Virtual Machine Management

* View all Azure Virtual Machines
* Monitor VM power status (Running / Stopped / Deallocated)
* Start Virtual Machine
* Stop Virtual Machine
* Restart Virtual Machine
* Delete Virtual Machine
* View VM details (OS Type, Size, Location)

### 🔹 Resource Group Explorer

* List all Azure Resource Groups
* View resources inside selected Resource Group

### 🔹 Monitoring & Dashboard

* Real-time VM status count
* Auto refresh every 20 seconds
* Manual refresh button
* Health check endpoint (`/healthz`)

### 🔹 Security

* Admin login authentication
* Environment variable-based configuration
* Secure Azure SDK authentication using ClientSecretCredential

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* Azure SDK
* Gunicorn (Production server)

### Frontend

* HTML
* CSS
* JavaScript

### Cloud & Deployment

* Microsoft Azure
* Azure App Service (Linux)
* Azure Virtual Machines
* GitHub

---

## 🔗 APIs Used

The application uses Microsoft Azure SDK APIs:

### 🔹 Azure Identity

* `ClientSecretCredential`
* Used for secure authentication with Azure

### 🔹 Azure Compute Management

* `ComputeManagementClient`
* List Virtual Machines
* Start VM
* Stop VM
* Restart VM
* Delete VM
* Get VM details
* Get VM instance view (Power state)

### 🔹 Azure Resource Management

* `ResourceManagementClient`
* List Resource Groups
* List resources inside a Resource Group

---

## ⚙️ Project Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/akishorekumar-1728/Azure_Cloud_dashboard.git
cd Azure_Cloud_dashboard
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variables

Create a `.env` file:

```
FLASK_SECRET_KEY=your_secret
ADMIN_EMAIL=ADMIN-EMAIL
ADMIN_PASSWORD=ADMIN_PASSWORD
AZURE_TENANT_ID=your_tenant_id
AZURE_CLIENT_ID=your_client_id
AZURE_CLIENT_SECRET=your_client_secret
AZURE_SUBSCRIPTION_ID=your_subscription_id
```

---

### 5️⃣ Run Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

### 🌍 Deployment

Deployed on Azure App Service (Linux) using GitHub integration.

Health Check Endpoint:

```
/healthz
```

---

