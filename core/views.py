from django.shortcuts import redirect
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from conversation.models import Conversation
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
import datetime

@api_view(['GET'])
def index(request):
    request = UserProfiles.objects.all() # get all objects
    serializer = UserProfilesSerializer(request, many=True) # many=True is required for list of objects, many=False for single object
    return Response(serializer.data)

#Method to create a ride and view all the rides
#Path: /core/rides
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def rides(request):
    if request.method == 'GET':
        rides = Rides.objects.exclude(creator=request.user.pk) #Returns only the open rides that are not created by the current logged-in user
        time = datetime.datetime.now()
        for r in rides:
            if time>r.date_time:
                r.status = "Completed"
                r.save()
        new_rides = rides.filter(status="Open")
        serializer = RidesSerializer(new_rides, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data["creator"] = request.user.pk #Do not need to pass creator in the api call's body, it is automatically added
        serializer = CreateRidesSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Ride Created Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    """
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        data["creator"] = request.user.pk #Do not need to pass creator in the api call's body, it is automatically added
        rides = Rides.objects.get(id=request.data["id"])
        serializer = CreateRidesSerializer(rides, data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        ride = Rides.objects.get(id=request.data["id"])
        ride.delete()
        return Response({"Success": "Ride Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)"""
    



"""@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ratings(request):
    if request.method == 'GET':
        ride = Rides.objects.filter(creator=request.user, status="Completed")
        riderequest = RideRequests.objects.filter(passenger=request.user.pk, status = "Accepted")
        riderequest = riderequest.filter(~Q(ride__status="Completed"))
        riderequest = riderequest.values_list('ride', flat=True)
        for r in ride:
            ratings = Ratings.objects.filter(ride=r) #| Ratings.objects.filter(ride=riderequest)
            serializer += RatingsSerializer(ratings, many=True)
        #serializer = RatingsSerializer(ratings, many=True)
        #if serializer.is_valid():
        return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        data["user_rating"] = request.user.pk
        if data["ride_id"]:
            data["user_rated"] = Rides.objects.get(id=data["ride_id"]).creator.pk
        if data["ride_request_id"]:
            data["user_rated"] = RideRequests.objects.get(id=data["ride_request_id"]).passenger.pk
        serializer = CreateRatingsSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RatingsSerializer(ratings, data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        ratings = Ratings.objects.get(id=request.data["id"])
        ratings.delete()
        return Response({"Success": "Ratings Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT) """





@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])        
def riderequest(request):
    if request.method == 'GET':
        ride_requests = RideRequests.objects.filter(ride__creator = request.user.pk, status="Pending") | RideRequests.objects.filter(ride__creator = request.user.pk, status="Accepted")
        serializer = RideRequestsSerializer(ride_requests, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        data["ride"] = Rides.objects.get(id=data["ride"]).pk
        data["passenger"] = request.user.pk #Do not need to pass passenger (logged in user) in the api call's body, it is automatically added
        serializer = CreateRideRequestsSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Request created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RidesSerializer(rides, data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def myrides(request):
    user = request.user
    data = RideRequests.objects.filter(Q(passenger=user) | Q(ride__creator=user))
    serializer = RideRequestsSerializer(data, many=True)
    if serializer.is_valid():
        return JsonResponse(serializer.data, safe= False, status=status.HTTP_200_OK)
    return JsonResponse({'failed':"failed"},status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def myUserProfile(request):
    if request.method == 'GET':
        try:
            user = request.user
            data = UserProfiles.objects.get(user = user)
            serializer = UserProfilesSerializer(data, many=False)
            return JsonResponse(serializer.data)
        except:
            return JsonResponse({'failed':"failed"},status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data["user"] = request.user
        userprofile = UserProfiles.objects.get(user = request.user)
        serializer = UpdateUserProfilesSerializer(userprofile, data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            profile_serialize = UserProfilesSerializer(userprofile, many=False)
            return JsonResponse(profile_serialize.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
        if request.method == 'POST':
            data=JSONParser().parse(request)    
            serializer = UserSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                
                return Response({'Success': 'User created successfully'}, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def handle_request(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        ride = Rides.objects.get(id=data["ride_id"])
        riderequest = RideRequests.objects.get(id=data["request_id"])
        riderequest.status = data["status"]
        riderequest.save()
        if data["status"] == "Accepted":
            ride.seats -= 1
            ride.save()
            conversations = Conversation.objects.get(rides=ride)
            passenger = riderequest.passenger
            conversations.members.add(passenger)
        if ride.seats == 0:
            ride.status = "Closed"
            ride.save()
        return redirect("/core/riderequest/")