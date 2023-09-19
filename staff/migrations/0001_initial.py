# Generated by Django 4.2.3 on 2023-09-18 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефонный номер')),
                ('whatsapp', models.CharField(max_length=15, verbose_name='Whatsapp')),
                ('telegram', models.CharField(max_length=15, verbose_name='Telegram')),
            ],
        ),
        migrations.CreateModel(
            name='TypeVacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_vacancy', models.CharField(max_length=50, verbose_name='Тип вакансии')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, verbose_name='Позиция')),
                ('requirements', models.TextField(verbose_name='Требования')),
                ('type_vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='staff.typevacancy', verbose_name='Тип вакансии')),
            ],
        ),
    ]
