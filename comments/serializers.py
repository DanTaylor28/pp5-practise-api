from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # docstring here
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_image.url')
    is_comment_owner = serializers.SerializerMethodField()

    def get_is_comment_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'post', 'text', 'owner', 'is_comment_owner',
            'uploaded_at', 'updated_at', 'profile_id',
            'profile_image'
        ]
