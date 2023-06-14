from django.db import models
from django.contrib.auth.models import User

from main_app.models import Hotel 
from employee_app.models import Employee


# Create your models here.

class Guest(models.Model):
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    room_number = models.IntegerField()
    phone_number = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
    

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    number = models.IntegerField()
    is_available = models.BooleanField(default=True)



class Stay(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    is_checked_out = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.guest} - {self.check_in_date} - {self.check_out_date}"