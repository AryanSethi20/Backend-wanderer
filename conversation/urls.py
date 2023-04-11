from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('chat/<int:index>/', views.chat, name='chat'),
    path('sendchat/', views.sendchat, name='sendchat'),
    path('members/<int:index>/',views.members, name='members')
]