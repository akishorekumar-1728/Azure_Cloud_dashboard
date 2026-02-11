# **📌 Azure Cloud Dashboard – Project Overview**

**Azure Cloud Dashboard** is a *web-based dashboard application* designed to monitor and visualize Microsoft Azure cloud resources in a single, user-friendly interface. It allows administrators to view the status and performance of Azure services such as virtual machines and other cloud resources from one consolidated dashboard.([GitHub][1])

---

## **🧾 Project Statement**

The Azure Cloud Dashboard project aims to simplify cloud monitoring by creating a centralized web application that connects to Azure services to retrieve and display resource status. This dashboard helps cloud administrators quickly assess the health of critical infrastructure without navigating the Azure portal.([GitHub][1])

---

## **✨ Key Features**

✔ View real-time status of Azure Virtual Machines and other Azure resources
✔ Clean and responsive dashboard UI
✔ Single panel to monitor cloud infrastructure
✔ Helps administrators quickly evaluate resource status
✔ Easy to extend for additional Azure services
✔ Core monitoring features integrated in web interface([GitHub][1])

---

## **🛠️ Technology Stack**

### **Frontend**

* **HTML** – Page structure and layout
* **CSS** – Styling and responsive design([GitHub][1])

### **Backend**

* **Python (Flask)** – Serves the dashboard and handles API integration
  (based on presence of `app.py`)([GitHub][1])

### **Cloud**

* **Microsoft Azure Platform** – Cloud services being monitored
* **Azure APIs** – Used to fetch resource data (implied by project goal)

### **Testing**

* `test_auth.py` – Tests related to authentication
* `test_azure.py` – Tests validating Azure integration([GitHub][1])

---

## **🧩 APIs Used**

Although not explicitly shown in the README, based on the project structure and purpose, the following APIs would typically be used:

🔹 **Azure Resource Management API** – To list and fetch Azure resources
🔹 **Azure Monitor API** – To get metrics and statuses of virtual machines and services
🔹 **Azure Authentication API (AD)** – For securely accessing Azure resources from backend code

These REST APIs are integrated via Python to retrieve data and then shown on the dashboard.

---

## **📁 Code Files Explained**

| **File**            | **Purpose**                                                |               
| ------------------- | ---------------------------------------------------------- | 
| `app.py`            | Main Flask/Python server to serve dashboard and Azure data |               
| `README.md`         | Project overview and feature list                          |               
| `requirements.txt`  | Lists Python packages needed                               |               
| `test_auth.py`      | Unit tests for authentication flow                         |               
| `test_azure.py`     | Unit tests for Azure API integration                       |               
| `test-vm-1_key.pem` | Example/placeholder key file (likely for test VM)          |               
| `templates/`        | HTML templates used for dashboard UI                       | 

---

## **⚙️ Project Setup (Step-by-Step)**

1️⃣ **Clone the GitHub Repository**

```bash
git clone https://github.com/akishorekumar-1728/Azure_Cloud_dashboard.git
cd Azure_Cloud_dashboard
```

2️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Configure Azure Credentials**
Create Azure Service Principal and set environment variables:

```
AZURE_CLIENT_ID=
AZURE_CLIENT_SECRET=
AZURE_TENANT_ID=
AZURE_SUBSCRIPTION_ID=
```

4️⃣ **Run the Application**

```bash
python app.py
```

5️⃣ **Open Dashboard**
In your browser:

```
http://127.0.0.1:5000
```

---

## **🎓 Use Case**

This dashboard helps administrators monitor Azure resources without logging into the Azure portal. It provides a quick overview of services like virtual machines, helping identify issues and reducing time for manual checks.([GitHub][1])

---


