from rest_framework import serializers
from .models import Society, Building

class SocietySerializer(serializers.ModelSerializer):
	class Meta:
		model = Society
		fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Building
		fields = '__all__'