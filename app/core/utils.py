from datetime import datetime
from rest_framework.response import Response

from core.models import *
from core.serializers import *

def get_available_rooms_by(**data):
    start_date_str = data.get('start_date')
    end_date_str = data.get('end_date')
    city = data.get('city')
    hotel = data.get('hotel')
    available_rooms = Room.objects.all()
    if city:
        available_rooms = available_rooms.filter(hotel__city_name=city)

    if hotel:
        available_rooms = available_rooms.filter(hotel__name=hotel)
    
    if start_date_str and end_date_str:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

        available_rooms = available_rooms.exclude(booking__to_date__gt=start_date, booking__from_date__lt=end_date)
    
    serializer = RoomSerializer(available_rooms, many=True)
    return serializer.data
