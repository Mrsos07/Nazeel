from django.db import models
from django.contrib.auth.models import User
from main_app.models import Hotel
# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.hotel} - {self.position} - {self.name}"
    
