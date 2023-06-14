from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return self.name
    
