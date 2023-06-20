from django.db import models
from django.utils import timezone
from main_app.models import Hotel
from guest_app.models import Guest, Room
import os
import datetime
# Create your models here.

# Create Main Service Model
class MainService(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)#The name of the hotel have a relation to the Hotel class
    name_service = models.CharField(max_length=100)#The name of the service
    description_service = models.CharField(max_length=1000)#The description of the service
    time_on = models.DateTimeField(default=timezone.now())#The time on which the service was created
    time_off = models.DateTimeField(default=timezone.now())#The time off which the service was created
    image = models.ImageField(upload_to="images/", default="images/default.jpg")



    def __str__(self):
        """Return the model as a string"""
        return self.name_service


# Create Sub Service Model
class SubService(models.Model):
    # The main service have a relation to the MainService class
    main_service = models.ForeignKey(MainService, on_delete=models.CASCADE)
    name_service = models.CharField(max_length=100)  # The name of the service
    # The name of the catogory of the service
    catogory = models.CharField(max_length=100)
    price = models.IntegerField()  # The price of the service
    image = models.ImageField(
        upload_to="images/", default="images/default.jpg")


    def __str__(self):
        """Return the model as a string"""
        return str(f"{self.price},{ self.name_service}")

class SubServiceRequest(models.Model):
    # The sub service have a relation to the SubService class
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE)
    room = models.ForeignKey(Room,  on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)




class Review(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)



