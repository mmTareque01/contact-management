from rest_framework.decorators import api_view
from rest_framework import generics, response, status
from ..models import User
from ..serializers.update_serializers import UserUpdateSerializer


@api_view(['PUT'])
def UpdateUser(request, id):
    try:
        user = User.objects.get(userId=id)
        updateUserData = UserUpdateSerializer(user, data={
            "userName": request.data["userName"],
            "email": request.data["email"],
        })
        if updateUserData.is_valid():
            updateUserData.save()
            return response.Response(updateUserData.data, status=status.HTTP_200_OK)
        else:
            return response.Response({"detail": updateUserData.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return response.Response({"detail": e}, status=status.HTTP_400_BAD_REQUEST)
