from django.shortcuts import render
from rest_framework import viewsets

from accounts.models import User
from accounts.serializer import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

