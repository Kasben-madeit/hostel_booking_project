"""
Model definitions for the hostel booking API.

These models represent hostels, rooms, and bookings. Each hostel has
multiple rooms; each room can have many bookings over time. A booking
associates a user with a room for a given date range.
"""
from django.db import models
from django.contrib.auth.models import User


class Hostel(models.Model):
    """Represents a hostel located on campus.

    Attributes:
        name: Name of the hostel.
        description: Brief description of the hostel.
        address: Street address or campus location.
        location: General location or neighborhood description.
        amenities: List of amenities available at the hostel (free‑text).
        created_at: Timestamp of when the hostel was added to the system.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    amenities = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Hostels'

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    """Represents an individual room within a hostel.

    Attributes:
        hostel: Foreign key linking to the owning hostel.
        room_number: Identifier for the room (e.g., "A1", "101").
        capacity: Maximum number of occupants.
        price: Cost per night or per semester.
        is_available: Whether the room is currently available for booking.
        room_type: Optional type of room (e.g., single, double, suite).
    """
    hostel = models.ForeignKey(Hostel, related_name='rooms', on_delete=models.CASCADE)
    room_number = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    room_type = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = 'Rooms'
        unique_together = ('hostel', 'room_number')

    def __str__(self) -> str:
        return f"{self.hostel.name} - {self.room_number}"


class Booking(models.Model):
    """Represents a booking of a room by a user.

    Attributes:
        user: User who made the booking.
        room: Room being booked.
        start_date: Start date of the booking.
        end_date: End date of the booking.
        created_at: When the booking record was created.
        status: Status of the booking (e.g., pending, confirmed, cancelled).
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        verbose_name_plural = 'Bookings'
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.user.username} booking for {self.room} from {self.start_date} to {self.end_date}"