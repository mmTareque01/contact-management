from ..serializers.base_serializers import BaseSerializer
import re
from rest_framework import serializers
from ..models import User, CustomUser
from django.contrib.auth.hashers import make_password


# class UserRegistrationSerializer(BaseSerializer):
#     class Meta:
#         model = CustomUser

#     def create(self, validated_data):
#         # Hash the password before saving the user
#         validated_data['password'] = make_password(validated_data['password'])
#         return super().create(validated_data)

# serializers.py
# from rest_framework import serializers
# from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('userId', 'email', 'password', 'createdAt', 'updatedAt', 'isDeleted')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user



class ValidateUserdata(serializers.Serializer):
    userName = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    confirmPassword = serializers.CharField()
