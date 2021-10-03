from django.contrib import admin
from django.urls import path
from .views import SocietyViewSet, BuildingViewSet

urlpatterns = [
    path('societies/', SocietyViewSet.as_view({
		'get': 'list', 
		'post': 'create'
	})),
	path('societies/<str:pk>', SocietyViewSet.as_view({
		'get': 'retrieve',
		'put': 'update',
		'delete': 'destroy'
	})),
	path('buildings/', BuildingViewSet.as_view({
		'get': 'list',
		'post': 'create'
	})),
	path('buildings/<str:pk>', BuildingViewSet.as_view({
		'get': 'retrieve',
		'put': 'update',
		'delete': 'destroy'
	})),
]