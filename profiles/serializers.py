from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    # Enables owner field to display the username rather than a number
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'location', 'bio',
            'created_at', 'updated_at', 'profile_image',
        ]
