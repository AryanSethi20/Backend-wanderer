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

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
import json


def index(request,index):
    request = UserProfiles.objects.get(id=index)
    serializer = UserProfilesSerializer(request)
    return JsonResponse(serializer.data, safe = False)

def rides(request,ride):
    data = Rides.objects.filter(creator=ride)
    serializer = RidesSerializer(data, many=True)
    return JsonResponse(serializer.data, safe = False)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getUserinfo(request):
    user = request.user
    user_data = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    print(request.user)
    return Response(user_data)

@csrf_exempt
def Userprofile(request):
    if request.method =='POST':
        data = JSONParser().parse(request)
        serializer = UserProfilesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    else:
        return HttpResponse("failed")
    
@csrf_exempt
def login(request):
    if request.method =='POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = UserProfilesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    else:
        return HttpResponse("failed")
    

    
# Create your views here.