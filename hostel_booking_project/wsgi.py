"""
WSGI config for hostel_booking_project.

This exposes the WSGI callable as a module-level variable named ``application``.
"""
import os

from django.core.wsgi import get_wsgi_application  # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostel_booking_project.settings')

application = get_wsgi_application()