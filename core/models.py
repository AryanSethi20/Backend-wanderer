from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    avg_rating = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = ("User Profile")

    def __str__(self):
        return f"{self.user}"
    

class Rides(models.Model):
    creator = models.ForeignKey(User, related_name='rides', on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    CHOICES = (
        ('Taxi', 'Taxi'),
        ('Personal Car', 'Personal Car'),
    )
    type = models.CharField(max_length=15, choices=CHOICES, default='Personal Car')
    date_time = models.DateTimeField()
    recurring = models.BooleanField()
    seats = models.IntegerField()

    class Meta:
        verbose_name = ("Ride")
        get_latest_by = ["date_time"]

    def __str__(self):
        return f"{self.origin} to {self.destination}"
    


class RideRequests(models.Model):
    ride = models.ForeignKey(Rides, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField()

    class Meta:
        verbose_name = ("Ride Request")

    def __str__(self):
        return f"{self.passenger} requests to ride with {self.ride}"
    
class Ratings(models.Model):
    user_rating = models.ForeignKey(User, related_name='user_rating', on_delete=models.CASCADE)
    user_rated = models.ForeignKey(User, related_name='user_rated', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = ("Rating")

    def __str__(self):
        return f"{self.user_rating} rated {self.user_rated}"