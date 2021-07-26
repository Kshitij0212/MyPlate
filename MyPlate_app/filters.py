from django.contrib.auth.models import User
import django_filters
from django_filters import CharFilter
from .models import FoodItems, Previous_records 


class FoodFilter(django_filters.FilterSet):
    food_name = CharFilter(field_name = 'name',lookup_expr = 'icontains', label='Search food items')

    class Meta :
        model = FoodItems
        fields = ('food_name',)
