# 🚀 Azure Cloud Dashboard (DevSecOps Enabled)

## 📌 Project Overview

Azure Cloud Dashboard is a **web-based cloud management and DevSecOps monitoring platform** built using Python and Flask. It allows users to securely manage and monitor Microsoft Azure Virtual Machines and Resource Groups from a centralized dashboard.

The project has been enhanced with **monitoring, cost optimization, security scanning, and DevOps CI/CD capabilities**, making it suitable for real-world cloud operations and final-year evaluation.

---

## 🎯 Key Objectives

* Centralized Azure resource management
* Real-time VM monitoring
* Cost optimization through idle resource detection
* Security compliance scanning
* Automated reporting and DevOps integration

---

## ✨ Features

### 🔹 1. Virtual Machine Management

* View all Azure Virtual Machines
* Start / Stop / Restart VMs
* Delete Virtual Machines
* View VM details (OS, size, region)
* Real-time VM power status tracking

---

### 🔹 2. Resource Group Explorer

* List all Azure Resource Groups
* View resources inside each group

---

### 🔹 3. Monitoring Dashboard 📊

* Real-time VM status overview
* CPU usage monitoring (Azure Monitor integration)
* Auto-refresh dashboard
* VM health and uptime tracking
* Interactive charts (Chart.js)

---

### 🔹 4. Alerts System 🚨

* High CPU usage alerts (>80%)
* VM down alerts
* Idle VM detection alerts
* Severity-based alert classification (Low / Medium / High)

---

### 🔹 5. Cost Optimization 💰

* Idle VM detection (low CPU usage)
* Cost-saving recommendations
* Running vs Idle VM analysis
* Estimated cost optimization insights

---

### 🔹 6. Security Compliance Scanner 🔐

* NSG open port detection (22, 3389, 80, 443)
* Public IP exposure detection
* Storage account public access check
* Risk scoring system (Low / Medium / High)
* Security scan reporting

---

### 🔹 7. Reporting System 📄

* Export reports in CSV format
* Security scan reports
* Cost optimization reports
* Audit-friendly logs

---

### 🔹 8. DevOps & CI/CD ⚙️

* GitHub Actions pipeline integration
* Automated deployment support
* Health check endpoint (`/healthz`)
* Environment-based configuration
* Logging support

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* Azure SDK (Compute + Resource + Monitor)
* Gunicorn (Production server)

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js (for visualization)

### Cloud & DevOps

* Microsoft Azure
* Azure App Service (Linux)
* Azure Virtual Machines
* GitHub Actions
* Docker (optional containerization)

---

## 🔗 Azure APIs Used

* **Azure Identity**

  * `ClientSecretCredential` (secure authentication)

* **Azure Compute Management**

  * VM lifecycle operations (Start/Stop/Restart/Delete)
  * VM instance view (power state)

* **Azure Resource Management**

  * Resource Group listing
  * Resource inventory management

* **Azure Monitor Query**

  * VM CPU performance metrics

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

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
FLASK_SECRET_KEY=your_secret_key

ADMIN_EMAIL=your_admin_email
ADMIN_PASSWORD=your_admin_password

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

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment

* Deployed using **Azure App Service (Linux)**
* CI/CD enabled via **GitHub Actions**
* Supports containerization via **Docker (optional)**

Health Check Endpoint:

```
/healthz
```

---

## 📊 Project Architecture

```
Flask App
   ↓
Azure SDK Integration
   ↓
Azure VM / Resource / Monitor APIs
   ↓
Dashboard UI (HTML + JS)
   ↓
Monitoring + Security + Cost Modules
```

---

## 📸 Screenshots

![alt text](<Screenshot 2026-06-28 175211.png>) 
![alt text](<Screenshot 2026-06-28 175231.png>) 
![alt text](<Screenshot 2026-06-28 175251.png>) 
![alt text](<Screenshot 2026-06-28 175306.png>) 
![alt text](<Screenshot 2026-06-28 175341.png>) 
![alt text](<Screenshot 2026-06-28 175403.png>)

---

## 🧠 Future Enhancements

* Kubernetes (AKS) integration
* AI-based cost prediction
* Auto-healing VM system
* Multi-cloud support (AWS + GCP)

---

## 👨‍💻 Author

**A. Kishore Kumar**
🎓 B.Tech IT Student

🔗 LinkedIn:
[https://www.linkedin.com/in/a-kishore-kumar-ba310a291](https://www.linkedin.com/in/a-kishore-kumar-ba310a291)

