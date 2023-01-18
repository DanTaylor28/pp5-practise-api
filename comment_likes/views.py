from django.shortcuts import render
from .models import CommentLike
from .serializers import CommentLikeSerializer
from rest_framework import generics
from drf_api.permissions import IsPostOwnerOrReadOnly


class CommentLikeList(generics.ListCreateAPIView):
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all().order_by('-created_at')

    # cannot like comments without this function
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentLikeDetail(generics.RetrieveDestroyAPIView):
    serializer_class = CommentLikeSerializer
    permission_classes = [IsPostOwnerOrReadOnly]
    queryset = CommentLike.objects.all()
