from django.contrib.auth.models import User
from django.db import models
from main_app.models import Hotel
from employee_app.models import Employee

# Create your models here.


class Room(models.Model):
    # the hotel have relationship with Hotel class that we import from main_app
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.IntegerField()  # the number of the room
    is_available = models.BooleanField(
        default=True)  # the room is available or not
    def __str__(self):
        return f"{self.room_number}"


# Create guest model
class Guest(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # the name of the guest # the room number
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()  # the phone number of the guest
    def __str__(self):
        """Returns a string representation of"""
        return f"{self.name}"


# create stay model
class Stay(models.Model):
    # the guest have relationship with Guest class
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    # the room have relationship with Room class
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()  # check in when the guest is checked in
    # check out when the guest is checked out
    check_out_date = models.DateTimeField()
    is_checked_out = models.BooleanField(
        default=False)  # the guest is checked out or not

    def __str__(self):
        """Returns a string representation of """
        return f"{self.guest} - {self.check_in_date} - {self.check_out_date}"
