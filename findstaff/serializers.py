from rest_framework import serializers
from .models import House, Room, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'item_number', 'room']


class RoomSerializer(serializers.ModelSerializer):
    item_name = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['id', 'room_name', 'house', 'item_name']



class HouseSerializer(serializers.ModelSerializer):
    room_set = RoomSerializer(many=True, read_only=True)
    class Meta:
        model = House
        fields = ['id', 'house_name', 'location', 'room_set']



