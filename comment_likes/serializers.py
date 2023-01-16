from rest_framework import serializers
from .models import CommentLike, Comment
from django.db import IntegrityError


class CommentLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comment_text = serializers.ReadOnlyField(source='comment.text')

    class Meta:
        model = CommentLike
        fields = [
            'id', 'owner', 'comment', 'comment_text',
            'created_at'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'error': 'you cannot like a comment more than once'
            })
