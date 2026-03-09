"""
URL routing for the hostels app.

Defines routes for registration, authentication, and model viewsets
via DRF's DefaultRouter.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import HostelViewSet, RoomViewSet, BookingViewSet, RegisterView

router = DefaultRouter()
router.register('hostels', HostelViewSet, basename='hostel')
router.register('rooms', RoomViewSet, basename='room')
router.register('bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('', include(router.urls)),
]