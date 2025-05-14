from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from django_filters.filters import DateFromToRangeFilter
from django_filters import rest_framework as filters

class AdvertisementFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter()
    creator = filters.NumberFilter(field_name='creator_id')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator']

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
