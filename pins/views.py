from django.shortcuts import render
from .models import Pin
from .serializers import PinSerializer
from rest_framework import generics
from drf_api.permissions import IsPostOwnerOrReadOnly


class PinList(generics.ListCreateAPIView):
    serializer_class = PinSerializer
    queryset = Pin.objects.all()
