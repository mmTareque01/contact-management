from rest_framework import serializers
from ..models import CustomUser


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # exclude = ['isDeleted', 'createdAt', 'updatedAt']
        exclude = []