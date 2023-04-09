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
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from django.core.exceptions import *

# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated,])
def chat(request,index,other):
    user=request.user
    try:
        conversationdata = Conversation.objects.get(rides=index ,  members__in=[user,User.objects.get(id=other)])
        messagedata = ConversationMessage.objects.filter(conversation = conversationdata)
        serializer = ConversationMessageSerializer(messagedata, many=True)
        return JsonResponse(serializer.data, safe=False)
    except ObjectDoesNotExist:
        return HttpResponse("ObjectDoesNotExist")
    

