# Generated by Django 4.2.3 on 2023-09-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0003_alter_tariff_options_alter_tariff_price_per_km'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='price_per_km',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Цена за километр'),
        ),
    ]
