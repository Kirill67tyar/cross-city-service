# Generated by Django 4.2.3 on 2023-09-17 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='remark',
            field=models.CharField(blank=True, max_length=255, verbose_name='Примечания к заказу'),
        ),
    ]
