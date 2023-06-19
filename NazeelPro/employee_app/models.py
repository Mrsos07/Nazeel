from django.contrib.auth.models import User
from django.db import models
from main_app.models import Hotel

# Create your models here.

# create employee model
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)# user have one to one relationship with user that we import from django
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)# name of employee
    position = models.CharField(max_length=50)# position of employee

    def __str__(self):
        """Return string representation"""
        return f" {self.name}"


