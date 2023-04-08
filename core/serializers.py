from collections import OrderedDict
from .models import Rides, RideRequests, Ratings, UserProfiles
from django.contrib.auth.models import User
from rest_framework_json_api import serializers
from rest_framework import status
from rest_framework.exceptions import APIException


class CreateRidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rides
        fields = ['origin', 'destination', 'date_time', 'recurring', 'seats']
    
class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=5, write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

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
        fields = ['id', 'creator', 'origin', 'destination', 'date_time', 'recurring', 'seats']

class RideRequestsSerializer(serializers.ModelSerializer):
    ride = RidesSerializer()

    class Meta:
        model = RideRequests
        fields = '__all__'
        