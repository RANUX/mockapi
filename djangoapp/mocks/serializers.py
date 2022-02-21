from rest_framework import serializers
from .models import MockData

class MockDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = MockData
        fields = '__all__'
