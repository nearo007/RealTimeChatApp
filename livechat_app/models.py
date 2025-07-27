from django.db import models
from django.utils import timezone

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)

class Message(models.Model):
    value = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    user = models.CharField(max_length=30)
    room = models.ForeignKey(Room, null=False, default=0 , on_delete=models.CASCADE)
