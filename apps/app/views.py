from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from apps.app.pagination import BasePagination
from .models import Category, Product, Order, OrderItem
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, OrderItemSerializer
from .filters import ProductFilter, CategoryFilter, OrderFilter, OrderItemFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = CategoryFilter
    pagination_class = BasePagination
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'id']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = ProductFilter
    pagination_class = BasePagination
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name', 'id']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = OrderFilter
    pagination_class = BasePagination
    ordering_fields = ['created_at', 'updated_at', 'id']

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = OrderItemFilter
    pagination_class = BasePagination
    search_fields = ['product__name']
    ordering_fields = ['quantity', 'price', 'id']
