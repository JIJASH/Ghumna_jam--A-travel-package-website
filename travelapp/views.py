from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    
    
class CustomerViewSet(viewsets.ModelViewSet):
    
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    


class HotelViewSet(viewsets.ModelViewSet):
    
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer
 


