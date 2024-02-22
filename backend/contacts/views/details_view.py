from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, response, status
from ..models import Contact
from ..serializers.details_serializer import ContactDetailsSerializer


@api_view(['GET'])
def ContactDetails(request, id):
    try:
        contacts = Contact.objects.get(CId=id)
        extractedContacts = ContactDetailsSerializer(contacts).data

        if not len(extractedContacts):
            return response.Response({"status": "400", "message": "Not found"})

        return response.Response({"status": "20020", "user": extractedContacts})
    except Exception as e:
        print(e)
        return response.Response({"status": "400", "message": "Not found"})
