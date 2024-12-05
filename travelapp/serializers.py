from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['id','username','email','contact_number','address']
        
        
        
class CustomerSerializer(serializers.ModelSerializer):
    
    user=UserSerializer(read_only=True)
    
    class Meta:
        model=Customer
        fields=['id','user','first_name','middle_name','last_name','address','contact_number','gender']
        
        
        
class HotelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Hotel
        fields='__all__'
        
        
        
