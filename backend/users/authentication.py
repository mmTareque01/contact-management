# custom_auth_backends.py
from rest_framework_simplejwt.exceptions import TokenError
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework_simplejwt.tokens import Token
from django.contrib.auth.backends import ModelBackend
from .models import User
from django.contrib.auth.hashers import check_password
import jwt

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if check_password(password, user.password):
            return user
        return None


def authenticate_token(access_token):
    try:
        decoded_token = jwt.decode(access_token, None, False)
        # user_id = decoded_token.payload['user-id']
        # expiration_time = decoded_token.payload['exp']

        # Check if the token is expired
        # if expiration_time < timezone.now().timestamp():
        #     print("expired!")
        #     return None

        # # Retrieve the user using the user_id from the token
        # user = User().objects.get(userId=user_id)
        return "geting"

    except TokenError:
        # Invalid token
        print("out")
        return None

# custom_auth_backends.py
# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model
# from django.contrib.auth.hashers import check_password
# # from django.utils.translation import ugettext_lazy as _
# # from django.utils.translation import gettext_lazy as _

# class EmailBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(email=email)
#         except UserModel.DoesNotExist:
#             return None

#         if check_password(password, user.password):
#             return user
#         return None

#     def get_user(self, user_id):
#         UserModel = get_user_model()
#         try:
#             return UserModel.objects.get(pk=user_id)
#         except UserModel.DoesNotExist:
#             return None

#     def validate_token(self, token):
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(auth_token=token)
#             return user
#         except UserModel.DoesNotExist:
#             return None
