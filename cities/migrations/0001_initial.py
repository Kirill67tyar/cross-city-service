# Generated by Django 4.2.3 on 2023-10-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'города',
                'verbose_name_plural': 'город',
                'ordering': ('name',),
            },
        ),
    ]