# 📦 Subscription Management API

A simple and efficient API to manage subscriptions, customers, services, and payments — built with Django and Django REST Framework.

---

## 📌 Table of Contents

- [📖 About the Project](#-about-the-project)
- [🚀 Features](#-features)
- [⚙️ Tech Stack](#️-tech-stack)
- [📂 Project Structure](#-project-structure)
- [🛠️ Installation](#️-installation)
- [📡 API Endpoints](#-api-endpoints)
- [🛡️ Authentication & Security](#️-authentication--security)
- [🧪 Testing](#-testing)
- [📚 Documentation](#-documentation)
- [📌 Deployment](#-deployment)
- [🤝 Contributing](#-contributing)
- [📩 Contact](#-contact)

---

## 📖 About the Project

Subscription Management API is a backend system that helps businesses manage:

- 👤 Customers  
- 🛎️ Services  
- 🔄 Active/Expired Subscriptions  
- 💸 Payments linked to subscriptions  

It provides a clear REST API that can be integrated with any frontend, mobile app, or third-party system.

---

## 🚀 Features

✅ Full CRUD operations for Customers, Services, Subscriptions, and Payments  
✅ Token-based authentication  
✅ Auto-generated API docs using Swagger & Redoc  
✅ Access control middleware to restrict sensitive endpoints  
✅ Deployed and publicly accessible (via PythonAnywhere or similar)  
✅ Designed for real-world SaaS use cases  

---

## ⚙️ Tech Stack

- **Backend**: Django, Django REST Framework  
- **Authentication**: Token Authentication  
- **Documentation**: drf-yasg (Swagger / Redoc)  
- **Deployment**: PythonAnywhere  
- **Database**: SQLite (development), PostgreSQL (production-ready)






🛡️ Authentication & Security
Uses Token Authentication from Django REST Framework.

Middleware added to restrict access to sensitive paths like /admin/, /swagger/, /docs/ for unauthenticated users.

python
Copier
Modifier
# Example Middleware Path Blocking
restricted_paths = ['/admin/', '/swagger/', '/docs/', '/redoc/']
🧪 Testing
You can use tools like:

✅ Postman

✅ Swagger UI (/swagger/)

✅ Django Admin (/admin/)

To test all endpoints and flows.

📚 Documentation
Swagger: /swagger/

Redoc: /redoc/

Live Docs: /docs/

Auto-generated using drf-yasg.

📌 Deployment
The project is deployed on PythonAnywhere.
Sensitive endpoints are protected, and API access is available online for demo purposes.

🤝 Contributing
Want to suggest features or improve the API?

Fork the project

Create a new branch

Submit a Pull Request

Let’s build something awesome together!



---

## 📂 Project Structure

