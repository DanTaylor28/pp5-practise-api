from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # docstring here
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_image.url')
    is_comment_owner = serializers.SerializerMethodField()
    post_title = serializers.ReadOnlyField(source='post.title')

    def get_is_comment_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'post', 'post_title', 'text', 'owner',
            'is_comment_owner', 'uploaded_at', 'updated_at',
            'profile_id', 'profile_image'
        ]


class CommentDetailSerializer(CommentSerializer):
    # this serializer is necessary just so you dont have to
    # reselect the post when editing any comments
    post = serializers.ReadOnlyField(source='post.id')
