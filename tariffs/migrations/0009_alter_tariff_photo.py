# Generated by Django 4.2.3 on 2023-11-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0008_alter_tariff_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='photo',
            field=models.CharField(default='', max_length=40, verbose_name='URL к изображению'),
        ),
    ]
