# core/serializers.py
from rest_framework import serializers

from .models import Scale


class ScaleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "device_id",
            "custom_name",
            "created_at",
            "updated_at",
        )
        model = Post
