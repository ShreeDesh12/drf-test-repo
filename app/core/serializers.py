from rest_framework.serializers import ModelSerializer

from .models import *

class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        depth = 1

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
