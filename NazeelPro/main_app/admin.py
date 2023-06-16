from django.contrib import admin
from . models import Hotel
from service_app.models import MainService
from guest_app.models import Guest
from service_app.models import SubService

from guest_app.models import Guest, Stay, Room
from employee_app.models import Employee



# show the hotel information in the admin panel
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'location', 'image')
admin.site.register(Hotel, HotelAdmin)


# show the main service and sub service information in the admin panel

class SubServiceAdmin(admin.ModelAdmin):
    list_display = ('main_service','name_service','catogory','price','delivery_time','image')
admin.site.register(SubService,SubServiceAdmin)



class MainServiceAdmin(admin.ModelAdmin):
    list_display = ('name_service', 'description_service','image', 'time_on', 'time_off')
admin.site.register(MainService, MainServiceAdmin)


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'room', 'phone_number')
admin.site.register(Guest, GuestAdmin)



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','position')
admin.site.register(Employee,EmployeeAdmin)



class StayAdmin(admin.ModelAdmin):
    list_display = ('guest','room','check_in_date','check_out_date','is_checked_out')
admin.site.register(Stay,StayAdmin)



class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel','room_number','is_available')
admin.site.register(Room,RoomAdmin)

