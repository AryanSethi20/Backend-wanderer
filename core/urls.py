from django.urls import path

from . import views

urlpatterns = [
    path('rides/<int:ride>/', views.rides, name='rides'),
    path('UserProfile/', views.Userprofile, name='Userprofile'),
    path('<int:index>/', views.index, name='index'),
]