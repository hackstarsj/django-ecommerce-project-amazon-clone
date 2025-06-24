import django_filters
from DjangoEcommerceApp.models import Products

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = ['product_name' ,'brand', 'product_max_price', 'product_discount_price']
