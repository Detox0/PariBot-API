from API.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'rut', 'mail', 'age')


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'thread_id', 'date_time', 'user')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'content', 'response', 'conversation')


class Message_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message_type
        fields = ('id', 'name', 'message')
