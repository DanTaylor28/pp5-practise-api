from django.shortcuts import render
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics, filters
from drf_api.permissions import IsPostOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        num_of_comments=Count('comment', distinct=True),
        num_of_pins=Count('pins', distinct=True)
    ).order_by('-uploaded_at')

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    search_fields = [
        'title',
        'category__name',
        'owner__username']

    ordering_fields = [
        'num_of_pins',
        'num_of_comments'
    ]
    filterset_fields = [
        'owner__profile',
        'category__name',
        # will show posts from users the selected user is following
        'owner__followed__owner__profile',
        # will show posts the selected user has liked
        'pins__owner__profile'
    ]

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
