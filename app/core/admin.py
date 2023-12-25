from django.contrib import admin
from django.contrib.admin import ModelAdmin

from core.models import *

@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    exclude = []


@admin.register(Hotel)
class HotelAdmin(ModelAdmin):
    list_display = ['name', 'city_name']

@admin.register(Room)
class RoomAdmin(ModelAdmin):
    search_fields = ['hotel__name', 'hotel__city_name']
    list_display = ['id', 'room_type', 'hotel']
