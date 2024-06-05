from rest_framework import serializers
from .models import House, Room, Staff


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'staff_name', 'staff_number', 'room']


class RoomSerializer(serializers.ModelSerializer):
    staff_set = StaffSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['id', 'room_name', 'house', 'staff_set']



class HouseSerializer(serializers.ModelSerializer):
    room_set = RoomSerializer(many=True, read_only=True)
    class Meta:
        model = House
        fields = ['id', 'house_name', 'location', 'room_set']



