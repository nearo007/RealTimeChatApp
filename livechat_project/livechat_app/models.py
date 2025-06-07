from django.db import models
from django.utils import timezone

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=timezone.now())
    user = models.CharField(max_length=100)
    room_id = models.CharField(max_length=1000)
