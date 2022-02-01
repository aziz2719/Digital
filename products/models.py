from django.db import models


class Product(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    scope = models.CharField(verbose_name='Сфера применения', max_length=255, blank=True, null=True)
    caliber = models.FloatField(verbose_name='Диаметр', blank=True, null=True)
    length = models.IntegerField(verbose_name='Длина', blank=True, null=True)
    color = models.CharField(verbose_name='Цвет', max_length=255, blank=True, null=True)
    image = models.ImageField(verbose_name='Изображение', upload_to="media/images", null=True, blank=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title

    