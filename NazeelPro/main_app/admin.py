from django.contrib import admin

# Register your models here.
from . models import Hotel

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'location', 'image')


admin.site.register(Hotel, HotelAdmin)