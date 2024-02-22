from rest_framework import serializers
from ..models import User

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id', 'isDeleted', 'createdAt', 'updatedAt']





