from contacts.serializers.base_serializer import BaseSerializer
from ..models import Address, Contact


class AddressSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Address
        exclude = []


class CreateContactSerializer(BaseSerializer):
    address = AddressSerializer(required=False)

    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        if address_data:
            address = Address.objects.create(**address_data)
            validated_data['address'] = address
        return Contact.objects.create(**validated_data)
