from rest_framework import serializers, exceptions
from .models import Information


class CreateInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['id', 'number', 'name', 'domb', 'domr', 'duty']


class GetInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['id', 'number', 'name', 'domb', 'domr', 'duty']


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['id', 'number', 'name', 'domb', 'domr', 'duty']


class SearchInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['id', 'number', 'name', 'domb', 'domr']


class DutyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['domb', 'domr', 'duty']
