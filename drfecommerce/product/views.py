from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A Simple Viewset for viewing categories
    """

    queryset = Category.objects.all()

    def list(self, request: Request):
        serializer: ListSerializer = CategorySerializer(
            self.queryset,
            many=True,
        )
        return Response(serializer.data)
