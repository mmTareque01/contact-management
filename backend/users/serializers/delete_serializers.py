from ..serializers.base_serializers import BaseSerializer


class DeleteUserSerializer(BaseSerializer):
    def destroy(self, instance):
        instance.delete()
