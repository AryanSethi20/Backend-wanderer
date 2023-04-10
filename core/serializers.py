from collections import OrderedDict
from .models import Rides, RideRequests, UserProfiles
from django.contrib.auth.models import User
from rest_framework_json_api import serializers
from rest_framework import status
from rest_framework.exceptions import APIException

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=5, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'id']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class UserProfilesSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfiles
        fields = '__all__'
        
class RidesSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    class Meta:
        model = Rides
        fields = ['id', 'creator', 'origin', 'destination', 'date_time', 'recurring', 'seats', 'status', 'start_lat', 'end_lat']

class CreateRidesSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Rides
        fields = ['creator', 'origin', 'destination', 'types', 'date_time', 'recurring', 'seats', 'start_lat', 'end_lat']

class RideRequestsSerializer(serializers.ModelSerializer):
    ride = RidesSerializer()
    passenger = UserSerializer()

    class Meta:
        model = RideRequests
        fields = '__all__'

class CreateRideRequestsSerializer(serializers.ModelSerializer):
    ride = serializers.PrimaryKeyRelatedField(queryset=Rides.objects.all())
    passenger = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = RideRequests
        fields = ['ride', 'passenger', 'status']
"""
class RatingsSerializer(serializers.ModelSerializer):
    ride = RidesSerializer()
    user_rating = UserSerializer()
    user_rated = UserSerializer()
    class Meta:
        model = Ratings
        fields = '__all__'

class CreateRatingsSerializer(serializers.ModelSerializer):
    ride = serializers.PrimaryKeyRelatedField(queryset=Rides.objects.all())
    user_rating = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user_rated = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Ratings
        fields = ['user_rating', 'user_rated', 'rating']"""