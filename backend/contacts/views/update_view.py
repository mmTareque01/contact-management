from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, response, status
from ..models import Contact
from ..serializers.update_serializer import UpdateContactSerializer
from backend.config.responseConfig import resBody, resStatus
from ..serializers.base_serializer import ValidateContactData
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def UpdateContact(request, id):
    try:
        contact = Contact.objects.get(CId=id)
        isValidInputData = ValidateContactData(data=contact)
        # if not isValidInputData.is_valid():
        #     return response.Response(resBody({}, resStatus["invalidInput"], isValidInputData.errors), status=status.HTTP_406_NOT_ACCEPTABLE)

        updatedContactData = UpdateContactSerializer(
            contact, data=request.data)

        if not updatedContactData.is_valid():
            return response.Response(resBody({}, resStatus["updateFailed"], updatedContactData.errors()), status=status.HTTP_406_NOT_ACCEPTABLE)

        updatedContactData.save()
        return response.Response(resBody(updatedContactData.data, resStatus["updated"]))
    except Exception as e:
        print(e)
        return response.Response(resBody({}, resStatus["serverError"]), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
