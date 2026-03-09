"""
View definitions for the hostel booking API.

These views leverage Django REST Framework's generic classes and viewsets
to provide CRUD operations on hostels, rooms, and bookings.
The RegisterView allows user registration via POST. Authentication
uses DRF's token authentication scheme.
"""
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .models import Hostel, Room, Booking
from .serializers import (
    UserSerializer,
    RegisterSerializer,
    HostelSerializer,
    RoomSerializer,
    BookingSerializer,
)


class RegisterView(generics.CreateAPIView):
    """API view for user registration."""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class CustomAuthToken(ObtainAuthToken):
    """Return auth token along with user details."""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):  # type: ignore
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
        })


class HostelViewSet(viewsets.ModelViewSet):
    """Viewset for managing hostels."""
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

    def get_permissions(self):  # type: ignore
        """Restrict creation to admins; allow read for all authenticated users."""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class RoomViewSet(viewsets.ModelViewSet):
    """Viewset for managing rooms."""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_permissions(self):  # type: ignore
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):  # type: ignore
        """Ensure the room is linked to a hostel passed in the request."""
        serializer.save()


class BookingViewSet(viewsets.ModelViewSet):
    """Viewset for managing bookings.

    Users can list and create bookings; admin can view all. Regular
    users see only their bookings.
    """
    serializer_class = BookingSerializer

    def get_queryset(self):  # type: ignore
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=user)

    def perform_create(self, serializer):  # type: ignore
        serializer.save(user=self.request.user)

    def get_permissions(self):  # type: ignore
        if self.action in ['destroy', 'update', 'partial_update']:
            # Only the owner of the booking or admin can modify it
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]