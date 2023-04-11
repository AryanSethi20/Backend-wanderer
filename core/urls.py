from django.urls import path
from . import views

urlpatterns = [
    path('rides/', views.rides, name='rides'),
    path('myrides/', views.myrides, name='rides'),
    path('riderequest/', views.riderequest, name='Ride-Request'),
    path('user-info/', views.getUserinfo, name='User-info'),
    path('userprofile/', views.myUserProfile, name='User-profile'),
    path('alluserprofiles/', views.allUserProfiles, name='All-User-profile'),
    path('<int:index>/', views.index, name='index'),
    path('register/', views.signup, name='register'),
    path('handle-request/', views.handle_request, name='handle-request'),
]
