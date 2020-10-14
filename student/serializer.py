from rest_framework import serializers, exceptions
from .models import Information
from rest_framework import status
from ManageSystem.utils import ERROR_MESSAGE


class CreateInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['id', 'number', 'name', 'domb', 'domr']


class GetInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['id', 'number', 'name', 'domb', 'domr']


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['id', 'number', 'name', 'domb', 'domr']
