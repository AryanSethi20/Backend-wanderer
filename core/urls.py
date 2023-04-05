from django.urls import path
from . import views
from .views import ride

urlpatterns = [
    path('', views.index, name='index'),
    path('rides/', ride.as_view()),
]