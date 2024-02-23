from rest_framework.decorators import api_view
from rest_framework import generics, response, status
from ..models import CustomUser
# from ..serializers.delete_serializers import


@api_view(['DELETE'])
def DeleteUser(request, id):
    try:
        user = CustomUser.objects.get(userId=id)
        user.delete()
        return response.Response({"detail": "Product successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        print(e)
        return response.Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
