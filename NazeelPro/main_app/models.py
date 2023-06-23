from django.db import models

# create Hotel model


class Hotel(models.Model):
    name = models.CharField(max_length=100)  # hotel name
    city = models.CharField(max_length=100)  # hotel city
    location = models.CharField(max_length=100)  # hotel location
    image = models.ImageField(upload_to="images/", default="images/default.jpg")  # hotel image

    def __str__(self):
        """String for representing the Model object"""
        return str(f"{self.name},{ self.city}")
