# Generated by Django 4.2.3 on 2023-11-08 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0009_alter_tariff_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='URL к изображению'),
        ),
    ]