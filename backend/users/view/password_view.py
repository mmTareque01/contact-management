from rest_framework.decorators import api_view
from rest_framework import response, status
from ..models import CustomUser
from ..serializers.update_password_serializers import UpdatePasswordSerializer


@api_view(['PATCH'])
def UpdatePassword(request, id):
    try:
        user = CustomUser.objects.get(userId=id)
        updateUserData = UpdatePasswordSerializer(user, data={
            "password": request.data["password"],
        })
        if updateUserData.is_valid():
            updateUserData.save()
            return response.Response(updateUserData.data, status=status.HTTP_200_OK)
        else:
            return response.Response({"detail": updateUserData.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return response.Response({"detail": "failed"}, status=status.HTTP_400_BAD_REQUEST)
