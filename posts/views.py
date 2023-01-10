from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from drf_api.permissions import IsPostOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsPostOwnerOrReadOnly]
    queryset = Post.objects.all()
