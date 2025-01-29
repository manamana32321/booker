import django_filters
from core.models.calendar import Calendar
from core.models.reservation import Reservation
from core.models.resource import Resource


class CalendarFilter(django_filters.FilterSet):
    class Meta:
        model = Calendar
        fields = "__all__"


class ReservationFilter(django_filters.FilterSet):
    class Meta:
        model = Reservation
        fields = "__all__"


class ResourceFilter(django_filters.FilterSet):
    class Meta:
        model = Resource
        fields = "__all__"
        exclude = ["image"]
