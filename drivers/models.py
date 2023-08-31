from django.db import models

"""
class Drivers(models.Model)

    name
    contact
    car
    
Нужно составить модель CarClasses
т.е. таблица с классами машин

И непонятно, то ли её Orders привязывать к этой таблице, то ли Drivers

Нужно создать таблицу Tariff, она для тарифов, для клиентов

У каждого водителя по одной машине. Как сказала галя так, чтобы у водителя было 2 машине не бывает.
"""


class Driver(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name='Имя водителя'
    )
    contact = models.CharField(
        max_length=16,
        verbose_name='Телефон водителя'
    )
    car = models.CharField(
        max_length=255,
        verbose_name='Машина'
    )
    tariff = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена за километр'
    )
