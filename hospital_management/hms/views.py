from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User, Availability, Booking


# LOGIN
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.role == 'doctor':
                return redirect('/doctor/')
            elif user.role == 'patient':
                return redirect('/patient/')

        else:
            return HttpResponse("Invalid credentials")

    return render(request, 'login.html')


# REGISTER
from django.shortcuts import render, redirect
from .models import User

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(
            username=username,
            password=password,
            role=role
        )

        return redirect('/')   # ✅ IMPORTANT FIX

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


# BOOK SLOT
@login_required
def book_slot(request, slot_id):
    slot = Availability.objects.get(id=slot_id)

    Booking.objects.create(
        patient=request.user,
        doctor=slot.doctor,
        slot=slot
    )

    return redirect('patient_dashboard')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')
