import django_filters
from .models import Profile


class SellFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = ["surname", "telephone"]
