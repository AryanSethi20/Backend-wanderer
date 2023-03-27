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