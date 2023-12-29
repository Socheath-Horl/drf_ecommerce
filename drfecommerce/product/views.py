from django.db import connection
from drf_spectacular.utils import extend_schema
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer
from sqlparse import format

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
    lookup_field = "slug"

    def retrieve(self, request: Request, slug=None):
        serializer: ListSerializer = ProductSerializer(
            self.queryset.filter(slug=slug).select_related("category", "brand"),
            many=True,
        )
        data = Response(serializer.data)
        q = list(connection.queries)
        print(len(q))
        for qs in q:
            sqlformatted = format(str(qs["sql"]), reindent=True)
            print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
        return data

    @extend_schema(responses=ProductSerializer)
    def list(self, request: Request):
        serializer: ListSerializer = ProductSerializer(
            self.queryset,
            many=True,
        )
        return Response(serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<category>\w+)/all",
        url_name="all",
    )
    def list_product_by_category(self, request: Request, category=None):
        """
        Endpoint to return products by category
        """
        serializer: ListSerializer = ProductSerializer(
            self.queryset.filter(category__name=category),
            many=True,
        )
        return Response(serializer.data)
