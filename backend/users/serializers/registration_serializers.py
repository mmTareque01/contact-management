from rest_framework import serializers
from ..models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('userId', 'email', 'password',
                  'createdAt', 'updatedAt', 'isDeleted')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class ValidateUserdata(serializers.Serializer):
    userName = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    confirmPassword = serializers.CharField()
