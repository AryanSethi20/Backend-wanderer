from collections import OrderedDict
from .models import Conversation, ConversationMessage
from rest_framework_json_api import serializers
from rest_framework import status
from rest_framework.exceptions import APIException

class ConversationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        fields = ('rides', 'created_at', 'modified_at')

class ConversationMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConversationMessage
        fields = ('conversation', 'content', 'created_at', 'created_by')

