# Generated by Django 4.2.3 on 2023-11-10 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ('read', '-timestamp'), 'verbose_name': 'Обратная связь', 'verbose_name_plural': 'Обратная связь'},
        ),
    ]
