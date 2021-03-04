from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Eventlist(models.Model):
    postby = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    organizer = models.CharField(max_length=100)
    joiningfees = models.CharField(max_length=10)
    pricemoney = models.CharField(max_length=10)
    members = models.CharField(max_length=5, null=True)
    link = models.CharField(max_length=100)
    Eventtime = models.CharField(max_length=20)
    venue = models.TextField()
    StartingDate = models.DateTimeField(blank=False, null=True)
    Endingdate = models.DateTimeField(blank=False, null=True)
    Category = models.CharField(max_length=50, default="")
    numberofseats = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title


class EventBook(models.Model):
    userid = models.CharField(max_length=100)
    eventid = models.CharField(max_length=100)
    booking = models.BooleanField(default=False)
    booking_confirmed = models.BooleanField(default=False)
    attended = models.BooleanField(default=False)
    certificate = models.ImageField(
        default='coming_soon.jpg', null=True, blank=True, upload_to='certificates')

    def __str__(self):
        return f'user id : {self.userid}'
