from django.db import models
import datetime



class User(models.Model):
    name = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)


class Conversation(models.Model):
    dateTime = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Message(models.Model):
    content = models.TextField()
    response = models.BooleanField(default=False)
    conversation_id = models.ForeignKey(Conversation,on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Message_type(models.Model):
    name = models.CharField(max_length=50)
    Message = models.ForeignKey(Message,on_delete=models.CASCADE)

