from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models.resource import Resource
from core.serializers.resource import ResourceSerializer
from core.views.filters import ResourceFilter


class ResourceListCreateAPIView(ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filterset_class = ResourceFilter


class ResourceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
