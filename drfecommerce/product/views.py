from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A Simple Viewset for viewing categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request: Request):
        serializer: ListSerializer = CategorySerializer(
            self.queryset,
            many=True,
        )
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A Simple Viewset for viewing brands
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request: Request):
        serializer: ListSerializer = BrandSerializer(
            self.queryset,
            many=True,
        )
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A Simple Viewset for viewing products
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request: Request):
        serializer: ListSerializer = ProductSerializer(
            self.queryset,
            many=True,
        )
        return Response(serializer.data)
