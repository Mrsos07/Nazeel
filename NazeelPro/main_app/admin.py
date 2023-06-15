from django.contrib import admin
from . models import Hotel
from service_app.models import MainService
from guest_app.models import Guest
from service_app.models import SubService

# Register your models here.


# show the hotel information in the admin panel
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'location', 'image')

admin.site.register(Hotel, HotelAdmin)


# show the main service information in the admin panel
class MainServiceAdmin(admin.ModelAdmin):
    list_display = ('name_service', 'description_service', 'image','time_on','time_off')
admin.site.register(MainService, MainServiceAdmin)


class SubServiceAdmin(admin.ModelAdmin):
    list_display = ('main_service','name_service','catogory','price','delivery_time','image')

admin.site.register(SubService,SubServiceAdmin)


class GuestAdmin(admin.ModelAdmin):
    list_display = ('created_by','user','name','room_number','phone_number')
admin.site.register(Guest,GuestAdmin)