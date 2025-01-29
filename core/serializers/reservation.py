from rest_framework import serializers
from ..models.reservation import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
        depth = 1
