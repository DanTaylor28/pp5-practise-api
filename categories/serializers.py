from rest_framework import serializers
from .models import Category
from django.db import IntegrityError


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name', 'created_at'
        ]
