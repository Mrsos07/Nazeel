from django.contrib import admin
from . models import Hotel
from service_app.models import MainService
from guest_app.models import Guest, Stay, Room
from employee_app.models import Employee

# Register your models here.


# show the hotel information in the admin panel
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'location', 'image')


admin.site.register(Hotel, HotelAdmin)


# show the main service information in the admin panel
class MainServiceAdmin(admin.ModelAdmin):
    list_display = ('name_service', 'description_service',
                    'image', 'time_on', 'time_off')


admin.site.register(MainService, MainServiceAdmin)


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_number', 'phone_number')


admin.site.register(Guest, GuestAdmin)


admin.site.register(Employee)


admin.site.register(Stay)


admin.site.register(Room)
