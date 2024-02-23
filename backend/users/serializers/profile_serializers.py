from ..serializers.base_serializers import BaseSerializer

class UserProfileSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        # model = Contact  # Assuming you have a Contact model
        exclude = ["password"]