from rest_framework import serializers
from .models import Society

class SocietySerializer(serializers.ModelSerializer):
	class Meta:
		model = Society
		fields = '__all__'