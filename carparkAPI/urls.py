from django.urls import path
from . import views
from .views import carpark

urlpatterns = [
    path('', carpark, name='carpark'),
]