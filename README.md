# Hostel Booking API

This repository contains the backend code for a **Hostel Booking API**. It is built with
[Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/).

## Features

- User registration and token‑based authentication.
- CRUD operations for hostels and rooms (admin only for writes).
- Users can view available rooms and make bookings.
- Bookings are associated with the authenticated user.
- Simple permission model: only administrators can create or modify hostels and rooms; normal users can only manage their own bookings.

## Getting Started

1. Install dependencies (requires Python 3.10+):

   ```bash
   pip install -r requirements.txt
   ```

2. Apply migrations and create a superuser:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

3. Run the development server:

   ```bash
   python manage.py runserver
   ```

4. Access the API at `http://localhost:8000/api/` and the admin site at `http://localhost:8000/admin/`.

## API Endpoints

| Method | Endpoint                         | Description                                          |
|-------:|-----------------------------------|------------------------------------------------------|
| `POST` | `/api/register/`                 | Register a new user                                 |
| `POST` | `/api/login/`                    | Obtain an auth token                                 |
| `GET`  | `/api/hostels/`                  | List all hostels                                     |
| `POST` | `/api/hostels/`                  | Create a hostel (admin only)                         |
| `GET`  | `/api/hostels/{id}/`             | Retrieve a hostel                                     |
| `PUT`  | `/api/hostels/{id}/`             | Update a hostel (admin only)                         |
| `DELETE`| `/api/hostels/{id}/`            | Delete a hostel (admin only)                         |
| `GET`  | `/api/rooms/`                    | List all rooms                                       |
| `POST` | `/api/rooms/`                    | Create a room (admin only)                           |
| `GET`  | `/api/rooms/{id}/`               | Retrieve a room                                      |
| `PUT`  | `/api/rooms/{id}/`               | Update a room (admin only)                           |
| `DELETE`| `/api/rooms/{id}/`              | Delete a room (admin only)                           |
| `GET`  | `/api/bookings/`                 | List bookings for the current user                  |
| `POST` | `/api/bookings/`                 | Create a booking                                     |
| `GET`  | `/api/bookings/{id}/`            | Retrieve a booking                                   |
| `PUT`  | `/api/bookings/{id}/`            | Update a booking (admin only or owner)               |
| `DELETE`| `/api/bookings/{id}/`           | Cancel a booking (admin only or owner)               |

## License

This project is released under the MIT License.