from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User, Availability, Booking
from django.core.mail import send_mail
from django.conf import settings

# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.role == 'doctor':
                return redirect('doctor_dashboard')
            elif user.role == 'patient':
                return redirect('patient_dashboard')

        return HttpResponse("Invalid credentials")

    return render(request, 'login.html')


# REGISTER
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")

        User.objects.create_user(username=username, password=password, role=role)

        return redirect('login')

    return render(request, 'register.html')


# DOCTOR DASHBOARD
@login_required
def doctor_dashboard(request):
    if request.user.role != 'doctor':
        return HttpResponse("❌ Access Denied: Not a doctor")

    slots = Availability.objects.filter(doctor=request.user)
    bookings = Booking.objects.filter(doctor=request.user)

    if request.method == "POST":
        time = request.POST['time']
        Availability.objects.create(doctor=request.user, time=time)

    return render(request, 'doctor.html', {
        'slots': slots,
        'bookings': bookings
    })


# PATIENT DASHBOARD
@login_required
def patient_dashboard(request):
    if request.user.role != 'patient':
        return HttpResponse("❌ Access Denied: Not a patient")

    slots = Availability.objects.all()

    return render(request, 'patient.html', {'slots': slots})


# BOOK SLOT__pycache__/
@login_required
def book_slot(request, slot_id):
    slot = Availability.objects.get(id=slot_id)

    # prevent double booking (IMPORTANT)
    if Booking.objects.filter(slot=slot).exists():
        return HttpResponse("Slot already booked")

    booking = Booking.objects.create(
        patient=request.user,
        doctor=slot.doctor,
        slot=slot
    )

    # ✅ EMAIL PART (FIXED)
    if request.user.email:
        send_mail(
            subject="Appointment Booking Confirmed",
            message=f"""
Hello {request.user.username},

Your appointment is confirmed.

Doctor: {slot.doctor.username}
Slot: {slot.time}

Thank you for using our hospital system.
""",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[request.user.email],
            fail_silently=False,   # 👈 IMPORTANT for debugging
        )

        print("EMAIL SENT TO TERMINAL")

    return redirect('patient_dashboard')

# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')