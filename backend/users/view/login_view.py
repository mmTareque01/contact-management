from exifread import logger
from rest_framework.decorators import api_view
from rest_framework import  response, status
from ..serializers.login_serializers import LoginSerializer
from ..serializers.profile_serializers import UserProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from backend.config.responseConfig import resStatus, resBody
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['POST'])
def userLogin(request):
    try:
        login_data = request.data
        login_serializer = LoginSerializer(data=login_data)
        if not login_serializer.is_valid():
            return response.Response(resBody({}, resStatus["invalidInput"], login_serializer.errors), status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(email=login_data.get("email"),
                            password=login_data.get("password"))

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return response.Response(resBody({"user": UserProfileSerializer(user).data, 'accessToken': access_token}, resStatus["login"]))
        else:
            return response.Response(resBody(user, resStatus["loginFailed"]), status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        logger.error(f"An error occurred during login: {str(e)}")
        return response.Response(resBody({}, resStatus['serverError']), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
