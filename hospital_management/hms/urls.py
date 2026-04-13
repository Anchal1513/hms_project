from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),

    path('doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient/', views.patient_dashboard, name='patient_dashboard'),

    path('book/<int:slot_id>/', views.book_slot, name='book_slot'),
    path('logout/', views.logout_view, name='logout'),
]