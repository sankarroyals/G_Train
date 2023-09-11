import email
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from api import serializers
from api.models import User
from api.serializers import UserSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def signup(request):
    data = request.data
    if request.method == 'POST':
        user = User.objects.create(
            name=data['name'],
            email=data['email'],
            mobile=data['mobile'],
            password=make_password(data['password']),
        )
        serializer = UserSerializer(user, many=False)
        return Response("registered success")

@api_view(['GET'])
def getting_all_users(request):
    users =  User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)



        
    