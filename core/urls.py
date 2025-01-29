from django.urls import path
from .views import calendar, reservation, resource


urlpatterns = [
    path(
        "calendars/",
        calendar.CalendarListCreateAPIView.as_view(),
        name="calendar-list_create",
    ),
    path(
        "calendars/<int:pk>/",
        calendar.CalendarRetrieveUpdateDestroyAPIView.as_view(),
        name="calendar-retrieve_update_destroy",
    ),
    path(
        "reservations/",
        reservation.ReservationListCreateAPIView.as_view(),
        name="reservation-list_create",
    ),
    path(
        "reservations/<int:pk>/",
        reservation.ReservationRetrieveUpdateDestroyAPIView.as_view(),
        name="reservation-retrieve_update_destroy",
    ),
    path(
        "resources/",
        resource.ResourceListCreateAPIView.as_view(),
        name="resource-list_create",
    ),
    path(
        "resources/<int:pk>/",
        resource.ResourceRetrieveUpdateDestroyAPIView.as_view(),
        name="resource-retrieve_update_destroy",
    ),
]
