from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics


class ProfileList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
