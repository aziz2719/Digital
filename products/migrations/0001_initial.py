# Generated by Django 4.0.1 on 2022-01-31 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('scope', models.CharField(blank=True, max_length=255, null=True, verbose_name='Сфера применения')),
                ('caliber', models.FloatField(blank=True, null=True, verbose_name='Диаметр')),
                ('length', models.IntegerField(blank=True, null=True, verbose_name='Длина')),
                ('color', models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]