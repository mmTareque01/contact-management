from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, response, status
from ..models import Contact
from ..serializers.delete_serializer import DeleteContactSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def DeleteContact(request, id):

    try:
        contact = Contact.objects.get(CId=id)
        contact.delete()
        return response.Response({"detail": "Product successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        print(e)
        return response.Response({"detail": "Not found.", "error": e}, status=status.HTTP_404_NOT_FOUND)
