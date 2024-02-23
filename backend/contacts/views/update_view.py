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
    except Contact.DoesNotExist:
        return response.Response(
            {'error': 'Contact not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = UpdateContactSerializer(
        contact, data={**request.data, **{"user": request.user.id}})
    isValidInputData = ValidateContactData(data=request.data)
    if not isValidInputData.is_valid():
        return response.Response(resBody({}, resStatus["invalidInput"], isValidInputData.errors, "Invalid contact"), status=status.HTTP_406_NOT_ACCEPTABLE)

    if serializer.is_valid():
        serializer.save()
        return response.Response(resBody(serializer.data, resStatus["updated"]))
    return response.Response(resBody({}, resStatus["updateFailed"], serializer.errors()), status=status.HTTP_406_NOT_ACCEPTABLE)
