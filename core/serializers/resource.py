from rest_framework import serializers
from ..models.reservation import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = "__all__"
        depth = 1
