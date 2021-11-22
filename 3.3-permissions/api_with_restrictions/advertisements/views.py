from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements import filters
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from .permissions import Authorization


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    # queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = filters.AdvertisementFilter

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    permission_classes = [Authorization]
    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update"]:
    #         return [IsAuthenticated()]
    #     return []

    def get_queryset(self):
        queryset = Advertisement.objects.exclude(status='DRAFT')
        if self.request.user.is_authenticated:
            queryset_draft = Advertisement.objects.filter(status='DRAFT', creator=self.request.user)
            full_queryset = queryset.union(queryset_draft)
            return full_queryset
        else:
            return queryset
