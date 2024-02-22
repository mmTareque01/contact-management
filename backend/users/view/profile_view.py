from rest_framework.decorators import api_view
from rest_framework import generics, response, status
from ..models import User
from ..serializers.profile_serializers import UserProfileSerializer

@api_view(['GET'])
def GetUser(request, id):
    try:
        users = User.objects.get(userId=id, isDeleted=False)
        serializerData = UserProfileSerializer(users).data
        return response.Response({"status": "20020", "users": serializerData})
    except Exception as e:
        print(e)
        return response.Response({"status": "20020", "users": e})