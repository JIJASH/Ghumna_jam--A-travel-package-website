from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.

User=get_user_model()


@api_view(['POST'])
def login(request):
    email=request.data.get('email')
    password=request.data.get('password')
    user=authenticate(username=email,password=password)
    
    if user:
        token,_=Token.objects.get_or_create(user=user)
        return Response({
            'user':user.get_username(),
            'token':token.key
        })
    return Response("Invalid username or password")



@api_view(['POST'])
def register(request):
    serializer=UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email=serializer.validated_data.get('email')
    password=serializer.validated_data.get('password')
    user=User.objects.create_user(email=email,password=password)
    if user:
        send_mail(
            "Welcome To Ecommerce",
            "Hello " + user.email + " Welcome To Ecommerce",
            "zeus@gmail.com",
            [user.email],
            
            
        )   
        return Response('User has been registered')
    
    return Response('Something went wrong')
