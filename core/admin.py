from django.contrib import admin
from .models import Rides, RideRequests, UserProfiles
# Register your models here.
@admin.register(Rides)
class RidesAdmin(admin.ModelAdmin):
    list_display = ("creator", "origin", "destination", "date_time", "recurring", "seats", "status", "start_lat", "end_lat")
@admin.register(RideRequests)
class RideRequestsAdmin(admin.ModelAdmin):
    list_display = ("ride", "passenger", "status")
"""@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ("user_rating", "user_rated", "rating", "status")"""
@admin.register(UserProfiles)
class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "profile_pic", "date_of_birth", "address")