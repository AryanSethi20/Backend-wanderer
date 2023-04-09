from collections import OrderedDict
from .models import Conversation, ConversationMessage
from rest_framework_json_api import serializers
from rest_framework import status
from rest_framework.exceptions import APIException
from core.serializers import *

class ConversationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        fields = ('rides', 'created_at', 'modified_at')

class ConversationMessageSerializer(serializers.ModelSerializer):
    
    created_by = UserSerializer()
    class Meta:
        model = ConversationMessage
        fields = ('conversation', 'content', 'created_at', 'created_by')

class CreateConversationMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationMessage
        fields = ['conversation', 'content', 'created_by', 'created_at']
