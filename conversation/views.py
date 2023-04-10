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
        conversationdata = Conversation.objects.filter(rides=index ,  members=user).get(members=other)
        messagedata = ConversationMessage.objects.filter(conversation = conversationdata)
        serializer = ConversationMessageSerializer(messagedata, many=True)
        return JsonResponse(serializer.data, safe=False)
    except ObjectDoesNotExist:
        return HttpResponse("ObjectDoesNotExist")
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def sendchat(request):
    try:    
        data = JSONParser().parse(request)
        data["created_by"] = request.user.pk
        data["content"] = "hello"
        data["conversation"] = Conversation.objects.get(id=data["conversation_id"]).pk
        serializer = CreateConversationMessageSerializer(data=data, many=False)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Success': 'Message sent successfully'}, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        return Response({'Failed': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'Failed': 'Message failed to be sent'}, status=status.HTTP_400_BAD_REQUEST)