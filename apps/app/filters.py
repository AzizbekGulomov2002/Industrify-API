import django_filters
from .models import Product, Category, Order, OrderItem

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'category']

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name']

class OrderFilter(django_filters.FilterSet):
    created_at = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Order
        fields = ['created_at']

class OrderItemFilter(django_filters.FilterSet):
    order = django_filters.ModelChoiceFilter(queryset=Order.objects.all())
    product = django_filters.ModelChoiceFilter(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['order', 'product']
