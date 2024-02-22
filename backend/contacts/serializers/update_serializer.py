from contacts.serializers.base_serializer import BaseSerializer
from .details_serializer import AddressSerializer
from ..models import Address



class UpdateContactSerializer(BaseSerializer):
    address = AddressSerializer(required=False)

    class Meta(BaseSerializer.Meta):
        exclude = []

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        if address_data:
            if instance.address:
                instance.address.country = address_data.get(
                    'country', instance.address.country)
                instance.address.state = address_data.get(
                    'state', instance.address.state)
                instance.address.city = address_data.get(
                    'city', instance.address.city)
                instance.address.zipCode = address_data.get(
                    'zipCode', instance.address.zipCode)
                instance.address.others = address_data.get(
                    'others', instance.address.others)
                instance.address.save()
            else:
                address = Address.objects.create(**address_data)
                instance.address = address
                # print(1)

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phoneNumber = validated_data.get(
            'phoneNumber', instance.phoneNumber)
        instance.save()

        return instance
