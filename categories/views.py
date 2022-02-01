from rest_framework.viewsets import ModelViewSet

from categories import models

from categories import serializers 


class CategoryView(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class SectionView(ModelViewSet):
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer


class GroupView(ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer


class SubgroupView(ModelViewSet):
    queryset = models.Subgroup.objects.all()
    serializer_class = serializers.SubgroupSerializer


class CardView(ModelViewSet):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer