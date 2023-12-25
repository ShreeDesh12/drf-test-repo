from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import *
from .utils import get_available_rooms_by

class HotelAPI(ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

class RoomAPI(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class BookingAPI(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


@api_view(['GET'])
def available_rooms_api(request):
    available_rooms = get_available_rooms_by(data=request.query_params)
    return Response({'message': 'success', 'rooms': available_rooms})


# Create your views here.
