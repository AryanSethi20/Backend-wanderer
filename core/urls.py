from django.urls import path

from . import views

urlpatterns = [
    path('<int:index>', views.index, name='index'),
]