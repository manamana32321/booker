from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models.reservation import Reservation
from core.serializers.reservation import ReservationSerializer
from core.views.filters import ReservationFilter


class ReservationListCreateAPIView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filterset_class = ReservationFilter


class ReservationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
