from rest_framework import serializers

from .models import Brand, Category, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CategoryMinSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="name")

    class Meta:
        model = Category
        fields = ["category_name"]


class BrandMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = "__all__"


class ProductLineMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        exclude = ["id", "is_active", "product"]


class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandMinSerializer()
    # category = CategoryMinSerializer()
    brand_name = serializers.CharField(source="brand.name")
    category_name = serializers.CharField(source="category.name")
    product_line = ProductLineMinSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "name",
            "slug",
            "description",
            "brand_name",
            "category_name",
            "product_line",
        ]
