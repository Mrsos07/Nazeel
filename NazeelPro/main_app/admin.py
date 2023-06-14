from django.contrib import admin

# Register your models here.
from . models import Hotel
from service_app.models import MainService

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'location', 'image')


admin.site.register(Hotel, HotelAdmin)

class MainServiceAdmin(admin.ModelAdmin):
    list_display = ('name_service', 'description_service', 'image','time_on','time_off')

admin.site.register(MainService, MainServiceAdmin)