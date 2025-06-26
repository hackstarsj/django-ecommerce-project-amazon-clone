import django_filters
from DjangoEcommerceApp.models import Products, SubCategories

class ProductFilter(django_filters.FilterSet):
    subcategories_id=django_filters.ModelChoiceFilter(
        queryset=SubCategories.objects.all(),
        label='Subcategory'
    )

    search=django_filters.CharFilter(
        field_name='product_name',
        lookup_expr='icontains',
        label='Search Product'
    )

    class Meta:
        model = Products
        fields = {
            'subcategories_id':['exact'],
            'brand':['icontains'],  
            'product_max_price':['lte', 'gte'],
            'product_discount_price':['lte', 'gte'],
        }
