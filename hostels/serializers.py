"""
Serializers for the hostel booking API.

These classes transform model instances to and from JSON for the
API layer. The RegisterSerializer handles user creation with
password hashing, while other serializers expose necessary fields
for API consumption.
"""
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Hostel, Room, Booking


class UserSerializer(serializers.ModelSerializer):
    """Simplified representation of a user."""

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for registering new users.

    This serializer creates a user with a hashed password. Email is
    optional. Only the username and password are required.
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': False, 'allow_blank': True},
        }

    def create(self, validated_data):  # type: ignore
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
        )
        return user


class HostelSerializer(serializers.ModelSerializer):
    """Serializer for hostels.

    Lists all rooms by primary key. You can extend this to nest rooms
    by using RoomSerializer and setting many=True, read_only=True.
    """
    rooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Hostel
        fields = ['id', 'name', 'description', 'address', 'location', 'amenities', 'rooms']


class RoomSerializer(serializers.ModelSerializer):
    """Serializer for rooms."""
    hostel = serializers.ReadOnlyField(source='hostel.id')

    class Meta:
        model = Room
        fields = ['id', 'hostel', 'room_number', 'capacity', 'price', 'is_available', 'room_type']


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for bookings.

    It automatically assigns the current user to the booking upon creation.
    """
    user = serializers.ReadOnlyField(source='user.username')
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    class Meta:
        model = Booking
        fields = ['id', 'user', 'room', 'start_date', 'end_date', 'status', 'created_at']

    def create(self, validated_data):  # type: ignore
        request = self.context.get('request')
        user = request.user if request else None
        booking = Booking.objects.create(user=user, **validated_data)
        return booking