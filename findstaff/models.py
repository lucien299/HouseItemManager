from django.db import models

# Create your models here.

class House(models.Model):
    house_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.house_name

class Room(models.Model):
    room_name = models.CharField(max_length=50)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_name


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_number = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name

    class Meta:
        ordering = ['item_name']

