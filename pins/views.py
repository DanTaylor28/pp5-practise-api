from django.shortcuts import render
from .models import Pin
from .serializers import PinSerializer
from rest_framework import generics
from drf_api.permissions import IsPostOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class PinList(generics.ListCreateAPIView):
    serializer_class = PinSerializer
    queryset = Pin.objects.all().order_by('-created_at')

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    # cannot like posts without this function
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PinDetail(generics.RetrieveDestroyAPIView):
    serializer_class = PinSerializer
    permission_classes = [IsPostOwnerOrReadOnly]
    queryset = Pin.objects.all()
