from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, response, status
from ..models import Contact
from ..serializers.list_serializer import ContactListSerializer
from backend.config.responseConfig import resBody, resStatus


@api_view(['GET'])
def ContactList(request):
    # need to implement pagination over here
    try:
        contacts = Contact.objects.filter(isDeleted=False)
        extractedContacts = ContactListSerializer(contacts, many=True).data

        if not len(extractedContacts):
            return response.Response(resBody([], resStatus['dataNotFound']))

        return response.Response(resBody(extractedContacts, resStatus['dataFound']))
    except Exception as e:
        print(e)
        return response.Response(resBody([], resStatus['serverError']))

