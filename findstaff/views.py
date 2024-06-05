from django.shortcuts import render
from .models import House, Room, Staff
from .serializers import HouseSerializer, RoomSerializer, StaffSerializer
from rest_framework import viewsets

# Create your views here.
class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    def get_queryset(self):
        return self.queryset.all()
