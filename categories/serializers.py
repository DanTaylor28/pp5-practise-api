from rest_framework import serializers
from .models import Category
from django.db import IntegrityError


class CategorySerializer(serializers.ModelSerializer):
    # displays number of posts in each category
    num_of_posts = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'created_at', 'num_of_posts'
        ]
