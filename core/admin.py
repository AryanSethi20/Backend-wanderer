from django.contrib import admin
from .models import Rides, RideRequests, Ratings, UserProfiles
# Register your models here.
@admin.register(Rides)
class RidesAdmin(admin.ModelAdmin):
    list_display = ("creator", "origin", "destination", "date_time", "recurring", "seats")
@admin.register(RideRequests)
class RideRequestsAdmin(admin.ModelAdmin):
    list_display = ("ride", "passenger", "accepted")
@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ("user_rating", "user_rated", "rating", "comment")
@admin.register(UserProfiles)
class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "profile_pic", "avg_rating")