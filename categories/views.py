from django.shortcuts import render
from django.db.models import Count
from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics, permissions
from drf_api.permissions import IsAdminOrReadOnly


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.annotate(
        # adds up posts in each category, gets used in serializer
        num_of_posts=Count('post', distinct=True)
    )


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
