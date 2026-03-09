"""
Django admin configuration for hostel booking models.
"""
from django.contrib import admin
from .models import Hostel, Room, Booking


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'created_at')
    search_fields = ('name', 'location')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'hostel', 'capacity', 'price', 'is_available')
    list_filter = ('hostel', 'is_available')
    search_fields = ('room_number',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'start_date', 'end_date', 'status', 'created_at')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('user__username', 'room__room_number')


    snkldsk