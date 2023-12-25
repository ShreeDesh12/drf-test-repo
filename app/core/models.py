from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_type = models.CharField(max_length=50)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    from_date = models.DateField()
    to_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)

