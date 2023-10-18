from django.db import models

"""
И непонятно, то ли её Orders привязывать к этой таблице, то ли Drivers

Нужно создать таблицу Tariff, она для тарифов, для клиентов

У каждого водителя по одной машине. Как сказала галя так, чтобы у водителя было 2 машине не бывает.

Пробные варианты тарифов взято с сайта:

    Эконом(4 места+багаж) от 18 руб/км
    Комфорт (4 места+багаж) от 20 руб/км
    Бизнес (4 места+багаж) от 27 руб/км
    Минивены (до 10 мест+багаж) от 30 руб/км
    Автобусы (до 20 мест+багаж) от 60 руб/км
    
галин вариант:
    4 места:
        Эконм-27 км
        Ком -30 км
        Универсал -35
        Комфорт+ 42
        Бизнес от 65...смотря,какие машины
    Минивэн до 7 мест-51 руб км 
        После 8 мест 70 руб км
        5-10 мест
    Спринтер от 11 до 19 мест 
    120 руб км
    
    
    * два минивена на 7 и 8 мест
      можно сделать "Минивен стандартный" и "Минивен крупный"
      как названия
      
      ПОМЕТИТЬ, ЧТО ЕСТЬ ВОЗМОЖНОСТЬ ГРУЗОВЫХ ПЕРЕВОЗОК
      НО Т.К. ГАЛЯ ДЕЛЕГИРУЕТ ДРУГИМ ОПЕРАТОРАМ, ОНА ЦЕНУ ВЫСЧИТЫВАТЬ
      НЕ МОЖЕТ, ТАК ЧТО ДЛЯ ГРУЗОВЫХ ПЕРЕВОЗОК (ИЛИ АВТОБУСОВ БОЛЬШЕ 19)
      ЦЕНА ВЫСЧИТЫВАЕТСЯ ИНДИВИДУАЛЬНО
"""


class Tariff(models.Model):
    PASSENGER = 'PAS'
    MINIVAN = 'MIN'
    SPRINTER = 'SPR'
    BUS = 'BUS'
    TRUCK = 'TRU'

    QUANTITY_SEATS_CHOICE = (
        (PASSENGER, '4 места',),
        (MINIVAN, '5-10 мест',),
        (SPRINTER, '11-19 мест',),
        (BUS, '> 19 мест',),
        (TRUCK, 'Грузоперевозки',),
    )

    car_class = models.CharField(  # db_index может здесь и имеет смысл
        max_length=25,
        verbose_name='Класс машины'
    )
    quantity_seats = models.CharField(
        max_length=3,
        choices=QUANTITY_SEATS_CHOICE,
        default=PASSENGER,
        verbose_name='Количество сидений'
    )
    price_per_km = models.PositiveSmallIntegerField(
        # или Decimal?
        null=True,
        blank=True,
        verbose_name='Цена за километр'
    )
    photo = models.ImageField(  # models.URLField - здесь будет лучше
        upload_to='tariffs/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )

    marks = models.CharField(
        max_length=255,
        default='',
        verbose_name='Марки тарифа'
    )

    # * с другой стороны, количество записей в Tariff будет не велико,
    # и имеет ли смысл db_index и unique хотя бы с этой точки зрения
    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'
        ordering = ('pk',)

    def save(self, *args, **kwargs):
        # self.marks = str(list(self.drivers.values_list('car', flat=True))).lstrip('[').rstrip(']')
        self.marks = ', '.join(list(self.drivers.values_list('car', flat=True)))
        super().save(*args, **kwargs)

    def __str__(self):
        if self.price_per_km:
            return f'{self.pk}) {self.car_class} ({self.price_per_km} р. за км.)'
        return f'{self.pk}) {self.car_class}'
