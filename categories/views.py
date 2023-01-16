from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('-created_at')


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
