from django.urls import path
from . import views
from .views import ride

urlpatterns = [
    path('rides/<int:ride>/', views.rides, name='rides'),
    path('user-info/', views.getUserinfo, name='User-info'),
    path('<int:index>/', views.index, name='index'),
    path('register/', views.signup, name='register'),
]