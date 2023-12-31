from pprint import pprint as pp
from django.db import models

"""
class Drivers(models.Model)

    name
    contact
    car
    


И непонятно, то ли её Orders привязывать к этой таблице, то ли Drivers

Нужно создать таблицу Tariff, она для тарифов, для клиентов

У каждого водителя по одной машине. Как сказала галя так, чтобы у водителя было 2 машине не бывает.

Пробные варианты тарифов взято с сайта:

    Эконом(4 места+багаж) от 18 руб/км
    Комфорт (4 места+багаж) от 20 руб/км
    Бизнес (4 места+багаж) от 27 руб/км
    Минивены (до 10 мест+багаж) от 30 руб/км
    Автобусы (до 20 мест+багаж) от 60 руб/км
    
    
"""


class Driver(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name='Имя водителя'
    )
    contact = models.CharField(
        max_length=25,
        verbose_name='Телефон водителя'
    )
    car = models.CharField(
        max_length=100,
        verbose_name='Машина'
    )
    tariff = models.ForeignKey(
        # blank=True,
        null=True,
        to='tariffs.Tariff',
        on_delete=models.SET_NULL,
        related_name='drivers',
        verbose_name='Тариф'
    )

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'
        ordering = ('name',)

    def save(self, *args, **kwargs):
        if self.tariff:
            marks = self.tariff.marks.split(', ')
            if len(marks) < 5 and self.car not in marks:
                if marks[0] == '':
                    self.tariff.marks = self.car
                else:
                    self.tariff.marks += f', {self.car}'
                self.tariff.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        marks = self.tariff.marks.split(', ')
        if self.car in marks:
            marks.remove(self.car)
            self.tariff.marks = ', '.join(marks)
            self.tariff.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'{self.pk}) {self.name}'
