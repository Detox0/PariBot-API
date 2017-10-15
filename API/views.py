from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
import json
import apiai


CLIENT_ACCESS_TOKEN = 'e1dfd591f4af441cb799a4c198b044d5'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

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
        # post data
        data = JSONParser().parse(request)

        # save message
        if "conversation_id" not in data:
            # conversation_serializer = ConversationSerializer(data={"user": User.objects.get(pk=data["user_id"]) })
            conversation_serializer = ConversationSerializer(data={"user": data["user_id"]})
            if conversation_serializer.is_valid():
                conversation_serializer.save()
                print(conversation_serializer.data)
                data["conversation_id"] = conversation_serializer.data["id"]
            else:
                return JsonResponse(status=400)


        serializer = MessageSerializer(data=data)
        if (serializer.is_valid()):
            serializer.save()

        # analyse data

        request = ai.text_request()
        request.lang = 'es'
        request.query = data['content']

        # interpret data
        http_response = request.getresponse()
        response = json.loads(http_response.read())

        result = response['result']
        action = result.get('action')
        actionIncomplete = result.get('actionIncomplete', False)

        print(json.dumps(response, indent=2))

        # Make response
        paribot_response = {
            "message": response['result']['fulfillment']["speech"],
            "conversation_id": data["conversation_id"]
        }


        # perform actions
        if action is not None:
            if action == "list_seguros":
                parameters = result['parameters']
                paribot_response["message"] = "Tus seguros contratados son: Seguro automotriz, Seguro de invalidez y SOAP"



        # save response
        serializer = MessageSerializer(data={
            "response": True,
            "content": paribot_response["message"],
            "conversation_id": data["conversation_id"]
        })
        if (serializer.is_valid()):
            serializer.save()
        return JsonResponse(paribot_response, status=201)
