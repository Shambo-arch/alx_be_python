import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    search = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    in_stock = django_filters.BooleanFilter(field_name='stock_quantity', lookup_expr='gt', widget=django_filters.widgets.BooleanWidget())

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'search', 'in_stock']
