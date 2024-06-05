from django.shortcuts import render
from .models import House, Room, Item
from .serializers import HouseSerializer, RoomSerializer, ItemSerializer
from rest_framework import viewsets, generics


# Create your views here.
class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        '''根据名称查询物品'''
        researcher = self.request.query_params.get('item_name', None)
        if researcher is not None:
            return Item.objects.filter(item_name=researcher)
        return Item.objects.all()

