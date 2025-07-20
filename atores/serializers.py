from rest_framework import serializers
from .models import Atores


class AtoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atores
        fields = '__all__'


class AtoresDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atores
        fields = '__all__'
