
from django.urls import path
from . import views

app_name = 'guest_app'
urlpatterns = [
    path('sign_in',views.sign_in,name='sign_in')
]