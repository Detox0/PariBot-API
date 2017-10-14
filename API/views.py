from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import User,Message
from .serializers import UserSerializer, MessageSerializer


@csrf_exempt
def user_list(request):
    """

    List all users, or create a new one
    """

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


def user_detail(request, pk):
    """
        Retrieve, update or delete a user.
        """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)


def all_user_messages(request, pk):

    mensajes = []

    try:
        messages = Message.objects.filter(conversation__user__id=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        for message in messages:
            mensajes.append(MessageSerializer(message).data)

        #return JsonResponse(mensajes, safe=False)
        return JsonResponse({'messages': mensajes})

@csrf_exempt
def receive_message(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)

        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
