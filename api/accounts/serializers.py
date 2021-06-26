from rest_framework import serializers
from accounts.models import Organization


class GetOrganizationSerializer(serializers.ModelSerializer):
    """Получение списка организаций"""

    class Meta:
        model = Organization
        fields = '__all__'
