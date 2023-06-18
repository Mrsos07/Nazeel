
from django.urls import path
from . import views

app_name = 'employee_app'
urlpatterns = [
    path('',views.employee,name='employee'),
    path("add/guest/",views.add_guest,name="add_guest"),
    path("add/room/",views.add_room,name="add_room"),
    
]