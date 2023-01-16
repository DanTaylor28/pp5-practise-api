from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from rest_framework import generics, permissions
from drf_api.permissions import IsPostOwnerOrReadOnly


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    # I dont know why yet.. but you have to include this to be
    # able to post comments!
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentDetailSerializer
    permission_classes = [IsPostOwnerOrReadOnly]
    queryset = Comment.objects.all()
