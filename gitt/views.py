from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from gitt.models import Product
from gitt.serializers.product_serializer import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
