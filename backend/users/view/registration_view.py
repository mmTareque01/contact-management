from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, response, status
from ..models import User
from ..serializers.registration_serializers import UserRegistrationSerializer, ValidateUserdata
from backend.config.responseConfig import resStatus, resBody


from rest_framework.response import Response
from rest_framework import status
# from .serializers import UserRegistrationSerializer
from rest_framework import generics, permissions


@api_view(['POST'])
def CreateUser(request):
    try:
        user = request.data
        isValidUserData = ValidateUserdata(data=user)
        if not isValidUserData.is_valid():
            return response.Response(resBody({}, resStatus["invalidInput"], isValidUserData.errors), status=status.HTTP_401_UNAUTHORIZED)

        if user["password"] != user["confirmPassword"]:
            return response.Response(resBody({}, resStatus["invalidInput"], None, "Password & Confirm-password should be same!"), status=status.HTTP_401_UNAUTHORIZED)

        newUserData = UserRegistrationSerializer(data={
            "userName": user["userName"],
            "email": "maarufa@gmai.com",
            "password": user["password"],
        })

        if not newUserData.is_valid():
            return response.Response(resBody({}, resStatus['registrationFailed'], None, "Email already exist!"), status=status.HTTP_400_BAD_REQUEST)

        newUserData.save()
        return response.Response(resBody({}, resStatus['registered'], newUserData.data))

    except Exception as e:
        print(e)
        return response.Response(resBody({}, resStatus['serverError']))


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response.Response({'userId': str(user.userId)}, status=status.HTTP_201_CREATED)
