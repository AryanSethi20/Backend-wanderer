from collections import OrderedDict
from .models import Rides, RideRequests, Ratings, UserProfiles
from django.contrib.auth.models import User
from rest_framework_json_api import serializers
from rest_framework import status
from rest_framework.exceptions import APIException

class RidesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rides
        fields = ['id', 'creator', 'origin', 'destination', 'date_time', 'recurring', 'seats']

class CreateRidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rides
        fields = ['origin', 'destination', 'date_time', 'recurring', 'seats']
    

class RideRequestsSerializer(serializers.ModelSerializer):

    ride = serializers.PrimaryKeyRelatedField(queryset=Rides.objects.all())

    class Meta:
        model = RideRequests
        fields = '__all__'

class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'

class UserProfilesSerializer(serializers.ModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = UserProfiles
        fields = '__all__'