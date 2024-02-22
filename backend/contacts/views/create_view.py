from rest_framework import generics, response, status
from ..models import Contact
from ..serializers.create_serializer import CreateContactSerializer
from ..serializers.base_serializer import ValidateContactData
from backend.config.responseConfig import resStatus, resBody
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from users.authentication import EmailBackend,authenticate_token


@api_view(['POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def CreateContact(request):
    try:
        access_token = request.headers.get('Authorization').split(' ')[1]
        user = authenticate_token(access_token)
        print(user)
        conatct = request.data
        # backend = EmailBackend()
        # user = backend.validate_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4NjA4NzU2LCJpYXQiOjE3MDg2MDg0NTYsImp0aSI6ImYzMTMxNjk1Mzc4MDQ5ZWViNmQzZDVmOTJkOTIxNWFlIiwidXNlcl9pZCI6MTF9.lB9BqzOkmwyfP_LSx7YQXZCDtTg4mS71QaMi6CQ3PCc")
        # print("user : "+ user)
        isValidInputData = ValidateContactData(data=conatct)
        if not isValidInputData.is_valid():
            return response.Response(resBody({}, resStatus["invalidInput"], isValidInputData.errors), status=status.HTTP_401_UNAUTHORIZED)

        newContactData = CreateContactSerializer(data={
            "name": conatct["name"],
            "email": conatct["email"],
            "phoneNumber": conatct["phoneNumber"],
            "address": {
                "country": conatct["address"]["country"],
                "state": conatct["address"]["state"],
                "city": conatct["address"]["city"],
                "zipCode": conatct["address"]["zipCode"],
                "others": conatct["address"]["others"],
            },
        })

        if not newContactData.is_valid():
            return response.Response(resBody({}, resStatus["createdFailed"], newContactData.errors, "Duplicate contact!"), status=status.HTTP_401_UNAUTHORIZED)

        newContactData.save()
        return response.Response(resBody(newContactData.data, resStatus["created"]))
    except Exception as e:
        print(e)
        return response.Response(resBody({}, resStatus["serverError"]), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
