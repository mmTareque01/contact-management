from rest_framework import generics, response, status
from ..serializers.registration_serializers import UserRegistrationSerializer, ValidateUserdata
from backend.config.responseConfig import resStatus, resBody
from rest_framework import generics, permissions


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            user = request.data
            isValidUserData = ValidateUserdata(data=user)
            if not isValidUserData.is_valid():
                return response.Response(resBody({}, resStatus["invalidInput"], isValidUserData.errors), status=status.HTTP_401_UNAUTHORIZED)

            if user["password"] != user["confirmPassword"]:
                return response.Response(resBody({}, resStatus["invalidInput"], None, "Password & Confirm-password should be same!"), status=status.HTTP_401_UNAUTHORIZED)

            serializer = self.get_serializer(data={
                "userName": user["userName"],
                "email": user["email"],
                "password": user["password"],
            })

            if not serializer.is_valid():
                return response.Response(resBody({}, resStatus['registrationFailed'], serializer.errors(), "Email already exist!"), status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return response.Response(resBody({}, resStatus['registered'], serializer.data))

        except Exception as e:
            print(e)
            return response.Response(resBody({}, resStatus['serverError']))
