from django.shortcuts import render
from .models import Follower
from .serializers import FollowerSerializer
from rest_framework import generics
from drf_api.permissions import IsPostOwnerOrReadOnly


class FollowerList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all().order_by('-created_at')

    # cannot follow users without this function
    # It recognises the currently logged in user as the 'Owner' i think..
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
