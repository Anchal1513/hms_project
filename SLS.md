🏥 System Level Specification (SLS)
Hospital Management System (HMS)
📌 1. Introduction
1.1 Purpose

This document defines the System Level Specification (SLS) for the Hospital Management System (HMS). It describes the internal system design, architecture, modules, and data flow of the application.

1.2 Scope

The HMS is a web-based application designed to manage hospital operations such as patient records, doctor management, and appointment scheduling with role-based access control.

🏗️ 2. System Architecture

The system follows a three-tier architecture:

2.1 Presentation Layer (Frontend)
Built using HTML, CSS, and Bootstrap
Provides user interfaces for:
Login & Registration
Doctor Dashboard
Patient Dashboard

2.2 Application Layer (Backend)
Developed using Django
Handles:
Business logic (views.py)
URL routing (urls.py)
Authentication and authorization

2.3 Data Layer (Database)
Uses PostgreSQL / SQLite
Stores:
User information
Patient records
Doctor details
Appointment data

🧩 3. Module Design

The system is divided into the following modules:

3.1 Authentication Module
User registration and login
Role-based access control (Admin, Doctor, Patient)

3.2 Patient Module
Manage patient details
View appointment history

3.3 Doctor Module
Manage doctor profiles
Set specialization and availability

3.4 Appointment Module
Book appointments
View available time slots
Cancel/reschedule appointments

3.5 Admin Module
Manage doctors and patients
Monitor appointments
Full access via admin panel

🔄 4. System Workflow (Data Flow)
User sends request through web interface
Request is routed using urls.py
Appropriate function in views.py processes the request
Business logic interacts with models (models.py)
Data is stored/retrieved from database
Response is returned to the frontend

🗄️ 5. Database Design

5.1 Entities

User:

username,
password,
role

Patient:

id,
name,
age,
gender,
contact

Doctor:

id,
name,
specialization,
availability

Appointment:

id,
patient_id (Foreign Key),
doctor_id (Foreign Key),
date,
time,
status

5.2 Relationships
One Doctor → Many Appointments
One Patient → Many Appointments

🌐 6. URL / API Structure
/ → Home/Login
/register/ → User Registration
/login/ → Login
/doctor/ → Doctor Dashboard
/patient/ → Patient Dashboard
/book-appointment/ → Appointment Booking

🔗 7. Component Interaction
Appointment Booking Flow:
Patient logs in
Selects doctor
Chooses available slot
Request sent to backend
Appointment saved in database
Confirmation displayed

🔐 8. Security Design
Authentication handled by Django
Passwords stored securely (hashed)
Role-based authorization
Admin panel protected

⚙️ 9. Deployment Environment
Backend: Django server
Database: PostgreSQL / SQLite
Platform: Web browser
OS: Windows / Linux

⚠️ 10. Limitations
No online payment system
No notification feature
Basic UI design

🚀 11. Future Enhancements
Payment gateway integration
Email/SMS notifications
REST API support
Mobile application

📌 Conclusion

This System Level Specification provides a clear understanding of the internal structure, components, and workflow of the Hospital Management System. It ensures better scalability, maintainability, and understanding of the system design.
