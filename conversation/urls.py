from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('chat/<int:index>/<int:other>/', views.chat, name='chat'),
    path('sendchat/', views.sendchat, name='sendchat'),

]