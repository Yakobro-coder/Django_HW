from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()
    creator = filters.NumberFilter(field_name='creator__id')
    status = filters.ChoiceFilter

    # TODO: задайте требуемые фильтры
    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
