from rest_framework import serializers

from categories import models

from products.serializers import ProductSerializers


class SectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Section
        fields = ("id", "section_category", "section_sect")


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Group
        fields = ("id", "section", "name_group")


class SubgroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Subgroup
        fields = ("id", "group_subgroup", "subgroup")


class CardSerializer(serializers.ModelSerializer):
    product_card = ProductSerializers(many=True, read_only=True)
    card_subgroup = SubgroupSerializer(many=True, read_only=True)
    class Meta:
        model = models.Card
        fields = ("id", "card_category", "card_subgroup", "product_card")


class CategorySerializer(serializers.ModelSerializer):
    category_card = CardSerializer(many=True, read_only=True)
    class Meta:
        model = models.Category
        fields = (
            "id",
            "title",
            "description",
            "category_card",
        )