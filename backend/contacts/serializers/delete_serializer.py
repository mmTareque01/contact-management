from contacts.serializers.base_serializer import BaseSerializer


class DeleteContactSerializer(BaseSerializer):
    def destroy(self, instance):
        instance.delete()
