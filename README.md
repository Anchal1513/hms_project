🏥 Hospital Management System (HMS)
📌 Overview

The Hospital Management System (HMS) is a full-stack web application built using Django that streamlines hospital operations such as patient management, doctor scheduling, and appointment booking.

The system provides role-based dashboards for Admin, Doctors, and Patients, ensuring secure and efficient workflow management.

🚀 Key Features
👤 Authentication & Authorization
Secure login & registration system
Role-based access control (Admin / Doctor / Patient)
🏥 Patient Management
Patient registration and profile management
View appointment history
👨‍⚕️ Doctor Management
Doctor profiles and specialization tracking
Manage availability slots
📅 Appointment Booking
Book appointments with doctors
Slot-based scheduling system
Real-time availability handling
📊 Admin Dashboard
Manage doctors and patients
Monitor appointments
Full access via Django Admin panel
🛠️ Tech Stack
Technology	Description
Python	Core programming language
Django	Backend framework
HTML/CSS	Frontend structure
Bootstrap	UI styling
PostgreSQL	Database
📁 Project Structure
hospital_management/
│
├── hms/                     
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       ├── login.html
│       ├── register.html
│       ├── doctor.html
│       └── patient.html
│
├── hospital_management/     
│   ├── settings.py
│   └── urls.py
│
├── manage.py
└── db.sqlite3
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Anchal1513/hms_project.git
cd hms_project
2️⃣ Create Virtual Environment
python -m venv venv
3️⃣ Activate Environment
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate   # Mac/Linux
4️⃣ Install Dependencies
pip install -r requirements.txt
5️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
6️⃣ Create Superuser
python manage.py createsuperuser
7️⃣ Run Development Server
python manage.py runserver
🌐 Access the Application
Main App: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/
