from django.db import models

from main_app.models import Hotel

# Create your models here.

class MainService(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name_service = models.CharField(max_length=100)
    description_service = models.CharField(max_length=1000)
    time_on = models.DateTimeField()
    time_off = models.DateTimeField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return self.name_service
    

class SubService(models.Model):
    main_service = models.ForeignKey(MainService, on_delete=models.CASCADE)
    name_service = models.CharField(max_length=100)
    catogory = models.CharField(max_length=100)
    price = models.IntegerField()
    delivery_time = models.DateTimeField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")