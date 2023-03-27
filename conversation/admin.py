from django.contrib import admin
from .models import Conversation, ConversationMessage

admin.site.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("rides", "created_at", "modified_at")

admin.site.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = ("conversation", "content", "created_at", "created_by")