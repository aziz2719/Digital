from rest_framework import serializers

from products.models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "scope",
            "caliber",
            "length",
            "color",
            "image",
        )