from django.shortcuts import render
from django.db.models import Count
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from drf_api.permissions import IsPostOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        num_of_comments=Count('comment', distinct=True),
        num_of_pins=Count('pins', distinct=True)
    ).order_by('-uploaded_at')

# be aware! you didnt need this earlier but it suddenly stopped letting
# you post so you added it then
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsPostOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        num_of_comments=Count('comment', distinct=True),
        num_of_pins=Count('pins', distinct=True)
    )
