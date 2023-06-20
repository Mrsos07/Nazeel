from django.db import models
from guest_app.models import Guest, Room
from main_app.models import Hotel

# Create your models here.

# Create Main Service Model
class MainService(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)#The name of the hotel have a relation to the Hotel class
    name_service = models.CharField(max_length=100)#The name of the service
    description_service = models.CharField(max_length=1000)#The description of the service
    time_on = models.DateTimeField()#The time on which the service was created
    time_off = models.DateTimeField()#The time off which the service was created

    image = models.ImageField(upload_to="images/", default="images/default.jpg")#The image of the service 

    def __str__(self):
        """Return the model as a string"""
        return self.name_service
    

# Create Sub Service Model
class SubService(models.Model):
    main_service = models.ForeignKey(MainService, on_delete=models.CASCADE)#The main service have a relation to the MainService class
    name_service = models.CharField(max_length=100)#The name of the service 
    catogory = models.CharField(max_length=100)#The name of the catogory of the service 
    price = models.IntegerField()#The price of the service 
    delivery_time = models.DateTimeField()#The delivery time of the service 
    image = models.ImageField(upload_to="images/", default="images/default.jpg")#The image of the service 

    def __str__(self):
        """Return the model as a string"""
        return self.name_service