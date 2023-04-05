#Not sure about this views file, but still I have included it for now
"""
from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import UserProfilesSerializer, RidesSerializer, RideRequestsSerializer, RatingsSerializer
from .models import UserProfiles, Rides, RideRequests, Ratings
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class UserProfilesView(viewsets.GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    permission_classes = (IsAuthenticated,)
    queryset = UserProfiles.objects.all()
    serializer_class = UserProfilesSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }
    
    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)
    
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = UserProfilesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
"""

from .models import UserProfiles
from django.forms.models import model_to_dict
from .serializers import *
import json
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    request = UserProfiles.objects.all() # get all objects
    serializer = UserProfilesSerializer(request, many=True) # many=True is required for list of objects, many=False for single object
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def rides_list(request, creator, origin, destination, date_time, seats):
    if request.method == 'GET':
        rides = Rides.objects.all()
        serializer = RidesSerializer(rides, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        print(request.data)
        return Response(request.data)
    
"""     data = JSONParser().parse(request)
        serializer = RidesSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""


@api_view(['GET', 'PUT', 'DELETE'])        
def my_rides(request, creator):
    #/core/rides?query=creator
    rides = Rides.objects.get(creator=creator)
    if request.method == 'GET':
        rides_serializer = RidesSerializer(rides, many=True)
        
        return Response(rides_serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RidesSerializer(rides, data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        rides.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ride(generics.ListAPIView):
    queryset = Rides.objects.all()
    serializer_class = RidesSerializer

