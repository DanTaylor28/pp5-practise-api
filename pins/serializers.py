from rest_framework import serializers
from .models import Pin, Post
from django.db import IntegrityError


class PinSerializer(serializers.ModelSerializer):
    # remember to add docstrings for your classes!
    # displays owners name rather than an integer and automatically fills
    # owner field for us on form to like posts
    owner = serializers.ReadOnlyField(source='owner.username')
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Pin
        fields = [
            'id', 'owner', 'post', 'post_title',
            'created_at'
        ]

    # used to handle duplicate like attempts - has to be defined as create
    # with self and validated_data as arguments.
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'error': 'you cannot pin a post more than once'
            })
