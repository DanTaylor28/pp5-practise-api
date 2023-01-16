from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics
from drf_api.permissions import IsPostOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by('-created_at')


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsPostOwnerOrReadOnly]
    queryset = Profile.objects.all()
