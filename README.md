# 🏥 Hospital Management System (HMS)

## 📌 Overview
The Hospital Management System (HMS) is a Django-based web application designed to manage hospital operations efficiently. It provides separate dashboards for Admin, Doctors, and Patients with role-based access.

---

## 🚀 Features
- 👤 User Authentication (Doctor / Patient / Admin)
- 🏥 Patient Management System
- 👨‍⚕️ Doctor Management System
- 📅 Appointment Booking System
- 🔐 Role-Based Login System
- 📊 Admin Panel (Django Admin)
- 📋 Availability Slot Management

---

## 🛠️ Tech Stack
- Python 🐍
- Django 🌐
- HTML, CSS 🎨
- Bootstrap (UI styling)
- SQLite Database 🗄️

---

## 📁 Project Structure

hospital_management/
│
├── hms/ # Main Django app
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── admin.py
│
├── templates/ # HTML templates
│ ├── login.html
│ ├── register.html
│ ├── doctor.html
│ ├── patient.html
│
├── hospital_management/ # Project settings
│ ├── settings.py
│ ├── urls.py
│
├── manage.py
└── db.sqlite3


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/hms_project.git
cd hms_project
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install django
4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser
python manage.py createsuperuser
6️⃣ Run Server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
