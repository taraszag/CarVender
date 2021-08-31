import django_filters
from .models import Sellrequest


class SellFilter(django_filters.FilterSet):
    class Meta:
        model = Sellrequest
        fields = ["carmodelid","region","price","carbodyid","carstateid","gearboxid","drivetypeid","fueltypeid"]