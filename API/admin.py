from django.contrib import admin
from .models import User, Conversation, Message, Message_type

admin.site.register(User)
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Message_type)

