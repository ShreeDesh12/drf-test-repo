from django.urls import path, include
from rest_framework import routers

from .views import RoomAPI, BookingAPI, HotelAPI, available_rooms_api

room_api_router = routers.DefaultRouter()
room_api_router.register('rooms', viewset=RoomAPI, basename='rooms')

hotel_api_router = routers.DefaultRouter()
hotel_api_router.register(r'hotels', viewset=HotelAPI, basename='hotels')

booking_api_router = routers.DefaultRouter()
booking_api_router.register(r'booking', viewset=BookingAPI, basename='booking')

urlpatterns = [
    path('api/', include(room_api_router.urls)),
    path('api/', include(hotel_api_router.urls)),
    path('api/', include(booking_api_router.urls)),
    path('api/room/available', available_rooms_api)
]