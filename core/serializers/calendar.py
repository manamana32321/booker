from rest_framework import serializers
from ..models.calendar import Calendar
from .user import UserSerializer
from django.contrib.auth.models import User


class CalendarSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    ownerId = serializers.PrimaryKeyRelatedField(source='owner', queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Calendar
        fields = "__all__"
        depth = 1
