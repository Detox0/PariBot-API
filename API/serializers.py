from API.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'rut')


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'dateTime', 'user')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'content', 'response', 'conversation_id')


class Message_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message_type
        fields = ('id', 'name', 'message')
