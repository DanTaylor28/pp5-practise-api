from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # docstring here
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_image.url')
    is_comment_owner = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()

    def get_is_comment_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # include this to show the actual post title instead of just
    # the id value of the post :)
    def get_post(self, obj):
        return obj.post.title

    class Meta:
        model = Comment
        fields = [
            'id', 'post', 'text', 'owner', 'is_comment_owner',
            'uploaded_at', 'updated_at', 'profile_id',
            'profile_image'
        ]
