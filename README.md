

# ☁️ Azure Cloud Dashboard

## 📌 Project Statement

Azure Cloud Dashboard is a web-based cloud management application built using Flask and Azure SDK.
The system allows users to monitor and manage Azure Virtual Machines and Resource Groups in real-time through a secure, interactive dashboard deployed on Azure App Service.

The goal of this project is to simplify Azure infrastructure management using a custom-built cloud control panel with VM lifecycle operations and monitoring features.

---

## 🚀 Features

### 🔐 Authentication

* Secure login system (Session-based authentication)
* Environment variable-based Azure Service Principal authentication

### 🖥 Virtual Machine Management

* List all Virtual Machines in the subscription
* View VM details (size, OS type, location, power state)
* Start Virtual Machine
* Stop (Deallocate) Virtual Machine
* Restart Virtual Machine
* Delete Virtual Machine
* VM Status Count (Running / Stopped / Other)

### 📦 Resource Group Explorer

* List all Resource Groups
* View all resources inside a selected Resource Group
* Organized output (sorted by type and name)

### 📊 Monitoring & Health

* `/healthz` endpoint for Azure Health Check
* Application Insights integration
* App Service Log monitoring

### 🌐 Cloud Deployment

* Deployed on Azure App Service (Linux)
* CI/CD ready via GitHub
* Production URL enabled

---

## 🛠 Tech Stack

### 💻 Backend

* Python 3.11
* Flask
* Gunicorn (Production WSGI Server)

### ☁️ Cloud

* Microsoft Azure
* Azure App Service (Linux)
* Azure Virtual Machines
* Azure Resource Manager
* Azure Application Insights

### 🔐 Authentication & Identity

* Azure Service Principal
* Azure Identity SDK

### 📦 Azure SDK Libraries

* azure-identity
* azure-mgmt-compute
* azure-mgmt-resource
* azure-core

### 🎨 Frontend

* HTML
* CSS
* JavaScript
* Azure-themed UI design

---

## 🔌 APIs Used

### 🔹 Virtual Machine APIs

| Endpoint               | Method | Description       |
| ---------------------- | ------ | ----------------- |
| `/api/vms`             | GET    | List all VMs      |
| `/api/vm/details`      | GET    | Get VM details    |
| `/api/vm/start`        | POST   | Start VM          |
| `/api/vm/stop`         | POST   | Stop VM           |
| `/api/vm/restart`      | POST   | Restart VM        |
| `/api/vm/delete`       | POST   | Delete VM         |
| `/api/vm/status-count` | GET    | Get VM statistics |

### 🔹 Resource Group APIs

| Endpoint                 | Method | Description              |
| ------------------------ | ------ | ------------------------ |
| `/api/resource-groups`   | GET    | List all resource groups |
| `/api/resources?rg=name` | GET    | List resources inside RG |

### 🔹 Health Check

| Endpoint   | Method | Description                           |
| ---------- | ------ | ------------------------------------- |
| `/healthz` | GET    | App health check for Azure monitoring |

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
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create `.env` file (for local development):

```
AZURE_TENANT_ID=your_tenant_id
AZURE_CLIENT_ID=your_client_id
AZURE_CLIENT_SECRET=your_client_secret
AZURE_SUBSCRIPTION_ID=your_subscription_id
FLASK_SECRET_KEY=your_secret_key
```

⚠ In Azure App Service:
Go to
App Service → Settings → Environment Variables
Add the same variables there.

---

### 5️⃣ Run Locally

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

### 6️⃣ Production Deployment (Azure)

* Create Azure App Service (Python 3.11)
* Configure Startup Command:

```
gunicorn app:app
```

* Add Environment Variables in Azure
* Enable Health Check: `/healthz`
* Enable Application Insights

---

## 🌍 Live Deployment

Production URL:

```
https://azure-cloud-dashboard-kishore-htfrhpezh3cvfrc7.centralindia-01.azurewebsites.net
```

Health Check:

```
/healthz
```

---

## 🎯 Future Improvements

* Azure Entra ID (OAuth) Login
* Role-based Access Control
* Activity Logs Viewer
* CPU/Memory Monitoring Charts
* Cost Monitoring Dashboard
* Multi-user Management

---

## 👨‍💻 Author

**A Kishore Kumar**
Cloud & DevOps Enthusiast
Microsoft Azure | Python | Flask

---


