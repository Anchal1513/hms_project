from django.contrib import admin
from django.urls import path
from hms import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),

    path('doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient/', views.patient_dashboard, name='patient_dashboard'),

    path('book-slot/<int:slot_id>/', views.book_slot, name='book_slot'),
    path('logout/', views.logout_view, name='logout'),
]