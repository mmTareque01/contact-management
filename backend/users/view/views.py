from django.shortcuts import render
from exifread import logger
from rest_framework.decorators import api_view
from rest_framework import generics, response, status
from ..models import User
from ..serializers.base_serializers import UserSerializer
from django.contrib.auth import authenticate, login

# @api_view(['POST'])
# def Login(request):
#     user = User.objects.get(email=request.data['email'])
#     userData = UserSerializer(user).data
#     return response.Response({"status": "20020", "payload": userData})


