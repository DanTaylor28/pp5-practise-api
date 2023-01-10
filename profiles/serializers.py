from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    # Enables owner field to display the username rather than a number
    owner = serializers.ReadOnlyField(source='owner.username')
    is_post_owner = serializers.SerializerMethodField()

    def get_is_post_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'name', 'location', 'bio', 'owner',
            'is_post_owner', 'created_at', 'updated_at',
            'profile_image'
        ]
