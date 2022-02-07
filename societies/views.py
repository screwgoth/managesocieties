from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser

from .models import Society, Building
from .serializers import SocietySerializer, BuildingSerializer

class SocietyViewSet(viewsets.ModelViewSet):
	queryset = Society.objects.all()
	serializer_class = SocietySerializer
	
	def list(self, request):
		society = Society.objects.all()
		serializer = SocietySerializer(society, many=True)
		return Response(serializer.data)

	def create(self, request):
		serializer = SocietySerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def retrieve(self, request, pk=None):
		society = Society.objects.get(id=pk)
		serializer = SocietySerializer(society)
		return Response(serializer.data)

	
	def update(self, request, pk=None):
		society = Society.objects.get(id=pk)
		serializer = SocietySerializer(instance=society, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

	def destroy(self, request, pk=None):
		society = Society.objects.get(id=pk)
		society.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	
	def get_permissions(self):
		permission_classes = [permissions.IsAuthenticatedOrReadOnly]
		if self.action == 'list':
			permission_classes = [permissions.AllowAny]

		return [permission() for permission in permission_classes]

class BuildingViewSet(viewsets.ModelViewSet):

	queryset = Building.objects.all()
	serializer_class = BuildingSerializer
	
	def list(self, request):
		building = Building.objects.all()
		serializer = BuildingSerializer(building, many=True)
		return Response(serializer.data)

	def create(self, request):
		serializer = BuildingSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	
	def retrieve(self, request, pk=None):
		building = Building.objects.get(id=pk)
		serializer = BuildingSerializer(building)
		return Response(serializer.data)

	def update(self, request, pk=None):
		building = Building.objects.get(id=pk)
		serializer = BuildingSerializer(instance=building, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
	
	def destroy(self, request, pk=None):
		building = Building.objects.get(id=pk)
		building.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def get_permissions(self):
		permission_classes = [permissions.IsAuthenticatedOrReadOnly]
		if self.action == 'list':
			permission_classes = [permissions.AllowAny]
			
		return [permission() for permission in permission_classes]
	