
from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('',views.home,name='home'),
    path("history/",views.history,name="history"),
    path("services/",views.services,name="services"),
    path("about/",views.about,name="about"),
    path("order/",views.order,name="order"),
    path("maps/",views.maps,name="maps")
]