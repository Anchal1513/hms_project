from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class Availability(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.doctor.username} - {self.time}"


class Booking(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='doctor_bookings', on_delete=models.CASCADE)
    slot = models.ForeignKey(Availability, on_delete=models.CASCADE)

    test_field = models.CharField(max_length=100, default="Test")

    def __str__(self):
        return f"{self.patient.username} → {self.doctor.username}"