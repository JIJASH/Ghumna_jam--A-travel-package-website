from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import SimpleRouter

routers=SimpleRouter()
routers.register('user',UserViewSet,basename='user')
routers.register('customer',CustomerViewSet,basename='customer')
routers.register('hotel',HotelViewSet,basename='hotel')
urlpatterns = [
    
]+routers.urls