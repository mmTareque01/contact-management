from ..serializers.base_serializers import BaseSerializer
from django.contrib.auth.hashers import make_password


class UpdatePasswordSerializer(BaseSerializer):
    def update(self, instance, validated_data):
        # Hash the password before saving the user
        instance.password = make_password(validated_data.get('password'))
        instance.save()
        return instance
