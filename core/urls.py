from django.urls import path
from . import views

urlpatterns = [
    path('rides/', views.rides, name='rides'),
    path('user-info/', views.getUserinfo, name='User-info'),
    path('<int:index>/', views.index, name='index'),
    path('register/', views.signup, name='register'),
]