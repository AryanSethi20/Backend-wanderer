from django.urls import path
from .views import carpark, taxiAvailability

urlpatterns = [
    path('carpark/', carpark, name='carpark'),
    path('taxi/', taxiAvailability, name='TaxiAvailability')
]