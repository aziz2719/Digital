from rest_framework import viewsets

from products.models import Product

from products.serializers import ProductSerializers


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers