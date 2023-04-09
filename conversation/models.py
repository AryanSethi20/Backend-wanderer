from django.db import models
from django.contrib.auth.models import User
from core.models import Rides
from django.core.exceptions import ValidationError

class Conversation(models.Model):
    rides = models.ForeignKey(Rides, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)
    
class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created_at',)

    def clean(self):
        if self.created_by not in self.conversation.members.all():
            raise ValidationError('The creator of the message must be a member of the conversation.')