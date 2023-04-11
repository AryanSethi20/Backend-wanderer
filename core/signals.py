from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import UserProfiles, Rides
from conversation.models import Conversation

@receiver(post_save, sender=User, weak=False)
def report_uploaded(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        UserProfiles.objects.create(user=instance)

@receiver(post_save, sender=Rides, weak=False)
def report_uploaded(sender, instance, created, **kwargs):
    if created:
        Conversation.objects.create(rides=instance)
        conversation = Conversation.objects.get(rides=instance)
        conversation.members.add(instance.creator)
