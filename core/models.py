from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='', blank=True, null=True)
    #avg_rating = models.IntegerField(default=0)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    
    class Meta:
        verbose_name = ("User Profile")

    def __str__(self):
        return f"{self.user}"
    

class Rides(models.Model):
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    CHOICES = (
        ('Taxi', 'Taxi'),
        ('Personal Car', 'Personal Car'),
    )
    types = models.CharField(max_length=15, choices=CHOICES, default='Personal Car')
    date_time = models.DateTimeField()
    recurring = models.BooleanField()
    seats = models.IntegerField()
    start_lat = models.CharField(max_length=50, null=True)
    end_lat = models.CharField(max_length=50, null=True)
    CHOICES = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Completed', 'Completed')
    )
    status = models.CharField(max_length=10, choices = CHOICES, default='Open')

    class Meta:
        verbose_name = ("Ride")
        get_latest_by = ["date_time"]

    def __str__(self):
        return f"{self.origin} to {self.destination}"

class RideRequests(models.Model):
    ride = models.ForeignKey(Rides, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOICES = (
        ('Accepted', 'Accepted'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=CHOICES, default='Pending')

    class Meta:
        verbose_name = ("Ride Request")

    def __str__(self):
        return f"{self.passenger} requests to ride with {self.ride}"
    
"""class Ratings(models.Model):
    ride = models.ForeignKey(Rides, on_delete=models.CASCADE)
    user_rating = models.ForeignKey(User, related_name='user_rating', on_delete=models.CASCADE)
    user_rated = models.ForeignKey(User, related_name='user_rated', on_delete=models.CASCADE)
    RATE_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating = models.IntegerField(choices=RATE_CHOICES, default=0)
    CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=10, choices=CHOICES, default='Pending')

    class Meta:
        verbose_name = ("Rating")

    def __str__(self):
        return f"{self.user_rating} rated {self.user_rated}"""