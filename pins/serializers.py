from rest_framework import serializers
from .models import Pin
from django.db import IntegrityError


class PinSerializer(serializers.ModelSerializer):
    # displays owners name rather than an integer and automatically fills
    # owner field for us on form to like posts
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Pin
        fields = [
            'id', 'owner', 'post',
            'created_at'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detaail': 'possible duplicate'
            })
