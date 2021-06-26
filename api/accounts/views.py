from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, filters

from accounts.models import Organization
from api.accounts.serializers import GetOrganizationSerializer


class OrganizationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Класс для работы с организациями через API"""

    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    http_method_names = ["get"]
    queryset = Organization.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return GetOrganizationSerializer
        return GetOrganizationSerializer
