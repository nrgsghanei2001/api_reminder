from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Task
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    task_set = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Categori
        fields = '__all__'
