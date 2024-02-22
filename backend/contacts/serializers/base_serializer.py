from rest_framework import serializers
from ..models import Contact


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ['id', 'isDeleted', 'createdAt', 'updatedAt']


class ValidateContactData(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phoneNumber = serializers.CharField()
    