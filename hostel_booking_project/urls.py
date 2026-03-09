"""
URL configuration for hostel_booking_project.

Maps URL paths to views using Django's standard path and include functions.
It delegates API routes to the `hostels` app.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # API endpoints are namespaced under /api/
    path('api/', include('hostels.urls')),
]