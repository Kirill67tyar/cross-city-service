# Generated by Django 4.2.3 on 2023-09-08 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=50, verbose_name='Модель машины')),
                ('car_class', models.CharField(max_length=25, verbose_name='Класс машины')),
                ('quantity_seats', models.CharField(choices=[('PAS', '4 места'), ('MIN', '5-10 мест'), ('SPR', '11-19 мест'), ('BUS', '> 19 мест'), ('TRU', 'Грузоперевозки')], default='PAS', max_length=3, verbose_name='Количество сидений')),
                ('price_per_km', models.PositiveSmallIntegerField(verbose_name='Цена за километр')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
                'ordering': ('price_per_km',),
            },
        ),
    ]
