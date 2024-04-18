from api.models import Visit
from rest_framework import mixins, viewsets
from api.serializers.visit import VisitListSerializer, VisitRetrieveSerializer, VisitCreateSerializer, \
    VisitUpdateSerializer


class VisitView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return VisitListSerializer
        if self.action == 'retrieve':
            return VisitRetrieveSerializer
        if self.action == 'create':
            return VisitCreateSerializer
        if self.action == 'update':
            return VisitUpdateSerializer

    def get_queryset(self):
        return Visit.objects.all()
