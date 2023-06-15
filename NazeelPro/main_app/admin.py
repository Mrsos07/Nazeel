from django.contrib import admin
from . models import Hotel
from service_app.models import MainService
from guest_app.models import Guest
# Register your models here.


# show the hotel information in the admin panel
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'location', 'image')

admin.site.register(Hotel, HotelAdmin)


# show the main service information in the admin panel
class MainServiceAdmin(admin.ModelAdmin):
    list_display = ('name_service', 'description_service', 'image','time_on','time_off')

admin.site.register(MainService, MainServiceAdmin)

admin.site.register(Guest)