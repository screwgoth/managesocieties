from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url
from rest_framework import routers
from accounts.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
	path(r'', include(router.urls)),
]