from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models.calendar import Calendar
from core.serializers.calendar import CalendarSerializer
from core.views.filters import CalendarFilter


class CalendarListCreateAPIView(ListCreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    filterset_class = CalendarFilter


class CalendarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
