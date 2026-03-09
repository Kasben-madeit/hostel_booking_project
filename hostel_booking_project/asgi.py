"""
ASGI config for hostel_booking_project.

This exposes the ASGI callable as a module-level variable named ``application``.
"""
import os
from django.core.asgi import get_asgi_application  # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostel_booking_project.settings')

application = get_asgi_application()