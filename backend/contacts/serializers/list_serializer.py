from contacts.serializers.base_serializer import BaseSerializer
from ..models import Contact


class AddressSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Contact.address.field.related_model
        exclude = ["id"]


class ContactListSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        # model = Contact  # Assuming you have a Contact model
        exclude = ["id"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['address'] = AddressSerializer(instance.address).data
        return representation
