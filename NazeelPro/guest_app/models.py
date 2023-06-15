from django.db import models
from django.contrib.auth.models import User
from main_app.models import Hotel
from employee_app.models import Employee



# Create your models here.

# Create guest model
class Guest(models.Model):
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)#the user have relationship with User that we import from django
    name = models.CharField(max_length=50)#the name of the guest
    room_number = models.IntegerField()#the room number
    phone_number = models.IntegerField()#the phone number of the guest

    def __str__(self):
        """Returns a string representation of"""
        return f"{self.name}"
    
# Create room model
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)#the hotel have relationship with Hotel class that we import from main_app  
    number = models.IntegerField()# the number of the room
    is_available = models.BooleanField(default=True)# the room is available or not


# create stay model
class Stay(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)# the guest have relationship with Guest class 
    room = models.ForeignKey(Room, on_delete=models.CASCADE)# the room have relationship with Room class 
    check_in_date = models.DateTimeField()# check in when the guest is checked in 
    check_out_date = models.DateTimeField()# check out when the guest is checked out 
    is_checked_out = models.BooleanField(default=False)# the guest is checked out or not

    def __str__(self):
        """Returns a string representation of """
        return f"{self.guest} - {self.check_in_date} - {self.check_out_date}"


