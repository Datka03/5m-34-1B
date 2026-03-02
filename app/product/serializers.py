from rest_framework import serializers

from app.product.models import Category, Types, ProductImage, Product

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'crated_at']

class TypesSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = ['id', 'title', 'description', 'category', 'crated_at']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'product']

class ProductSerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'uuid', 'title', 'description',
            'category', 'types_product', 'created_at', 
            'price', 'first_image'
        ]

    def get_first_image(self, obj):
        fierts_img = obj.images.first()
        if fierts_img and fierts_img.image:
            request = self.context.get("request")
            url = fierts_img.image.url
            return request.build_absolute_uri(url) if request else url
        return None