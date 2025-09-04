from rest_framework import serializers
from .models import Product, Category, SubCategory


class GetProductsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image and hasattr(obj.image, "url"):
            return request.build_absolute_uri(obj.image.url)
        return None


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class GetAllCategorys(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
