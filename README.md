
---

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
ADMIN_EMAIL=ADMINEMAIL_id
ADMIN_PASSWORD=ADMIN_PASSWD
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
### Screenshots
<img width="1412" height="777" alt="Screenshot 2026-02-13 180249" src="https://github.com/user-attachments/assets/be42cd73-dca9-4b59-9c44-a9f7997ac40a" />
<img width="749" height="562" alt="Screenshot 2026-02-13 180317" src="https://github.com/user-attachments/assets/9341db08-77c6-416d-8ff1-c45a9502b611" />
<img width="1709" height="766" alt="Screenshot 2026-02-13 180352" src="https://github.com/user-attachments/assets/0d7e8cbf-9c7e-46e8-8ae2-3817e8bf5bec" />
<img width="1668" height="892" alt="Screenshot 2026-02-13 180419" src="https://github.com/user-attachments/assets/c16098f7-3fe8-4208-8802-16d4e4724716" />
<img width="1714" height="937" alt="Screenshot 2026-02-13 180445" src="https://github.com/user-attachments/assets/0b07e25e-d771-4ee2-80cf-ec61915097d4" />

👨‍💻 Author

A Kishore Kumar 🎓 B.Tech IT Student

LinkedIn: https://www.linkedin.com/in/a-kishore-kumar-ba310a291


