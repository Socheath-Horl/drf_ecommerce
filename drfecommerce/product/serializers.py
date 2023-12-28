from rest_framework import serializers

from .models import Brand, Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CategoryMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class BrandMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandMinSerializer()
    category = CategoryMinSerializer()

    class Meta:
        model = Product
        fields = "__all__"
