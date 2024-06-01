from django.db import models

# Create your models here.

class House(models.Model):
    house_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.house_name

class Room(models.Model):
    room_name = models.CharField(max_length=50)
    house_name = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_name


class Staff(models.Model):
    staff_name = models.CharField(max_length=50)
    staff_number= models.IntegerField()
    staff_room_name = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.staff_name

    class Meta:
        ordering = ['staff_name']





