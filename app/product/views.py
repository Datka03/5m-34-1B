from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import  ListAPIView, ListCreateAPIView

from app.product.serializers import (
    CategorySerializers, TypesSerilaizers,
    ProductSerializer
)
from app.product.models import Category, Types, Product

class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class TypesAPIView(ListAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesSerilaizers

class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



