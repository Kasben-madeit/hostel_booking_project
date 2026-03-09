#!/usr/bin/env python3
"""
manage.py

This is the command-line utility for administrative tasks. It mirrors
the standard Django-generated manage.py but does not rely on a local
installation of Django because your environment may not include the
framework by default. To run the server or perform migrations,
install Django and Django REST Framework in your environment and
execute this script with the appropriate arguments, for example:

    python manage.py runserver

"""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostel_booking_project.settings')
    try:
        from django.core.management import execute_from_command_line  # type: ignore
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your "
            "PYTHONPATH environment variable? Did you forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()