from django.db import models
from products.models import Product


class Category(models.Model):
    title = models.CharField("Название", max_length=255, blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("-id",)

    def __str__(self):
        return self.title


class Section(models.Model):
    section_category = models.ForeignKey(Category, models.SET_NULL, related_name='cat_sect', null=True, blank=True)
    section_sect = models.CharField('Раздел', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"
        ordering = ("-id",)

    def str(self):
        return self.section_sect


class Group(models.Model):
    section_group = models.ForeignKey(Section, models.SET_NULL, related_name='sec_gr', null=True, blank=True)
    name_group = models.CharField('Название', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        
    def str(self):
        return self.name_group


class Subgroup(models.Model):
    group_subgroup = models.ForeignKey(Group, models.SET_NULL, related_name='gr_sec', null=True, blank=True)
    subgroup = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = "Подгруппа"
        verbose_name_plural = "Подгруппы"

    def str(self):
        return self.subgroup


class Card(models.Model):
    card_category = models.ForeignKey(Category, models.SET_NULL, related_name='category_card', null=True, blank=True)
    subgroup_card = models.ForeignKey(Subgroup, models.SET_NULL, related_name='card_subgroup', null=True, blank=True)
    product_card = models.ManyToManyField(Product, related_name='card_product')

    class Meta:
        verbose_name = "Карточка товара"
        verbose_name_plural = "Карточка товаров"
        