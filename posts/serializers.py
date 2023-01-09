from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'title', 'caption',
            'uploaded_at', 'updated_at', 'image',
            'profile_id', 'profile_image'
        ]
