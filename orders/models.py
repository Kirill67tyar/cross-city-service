from decimal import Decimal

from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)


class Order(models.Model):
    NEW = 'new'
    READY = 'ready'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

    STATUS_CHOICE = (
        (NEW, 'Новый',),  # новый непрочитанный заказ
        (READY, 'Готов к исполнению',),  # заказ готов к исполнению (водитель найден)
        (COMPLETED, 'Завершён',),  # заказ завершён
        (CANCELLED, 'Отменён',),  # заказ по какой-то причине отменён
    )
    from_place = models.CharField(
        max_length=100,
        verbose_name='Место отправления'
    )
    to_place = models.CharField(
        max_length=100,
        verbose_name='Место прибытия'
    )
    # # travel_time - скорее всего не нужон
    # travel_time = models.PositiveSmallIntegerField(  # ? от 0 до 32767 (под большим вопросом, нужно ли)
    #     blank=True,
    #     null=True,
    #     verbose_name='Время в пути'
    # )
    distance = models.PositiveSmallIntegerField(
        blank=True,
        default=0,
        # null=True,  # ?!
        verbose_name='Дистанция в км.'
    )
    departure_time = models.DateTimeField(
        verbose_name='Время отправления'
    )
    driver = models.ForeignKey(  # внешний ключ на таблицу Drivers
        blank=True,
        null=True,
        to='drivers.Driver',
        on_delete=models.SET_NULL,
        related_name='orders',
        verbose_name='Водитель'
    )
    client = models.CharField(
        max_length=100,
        verbose_name='Клиент'
    )
    contact = models.CharField(
        max_length=150,
        verbose_name='Средство связи с клиентом'
    )
    remark = models.CharField(  # TextField
        # нужно для особых пометок:
        #  - перевоз инвалида
        #  - > 1 детского кресла
        #  - нестандартные средства связи
        #  - этничность водителя
        blank=True,
        max_length=255,
        verbose_name='Примечания к заказу'
    )
    baby_chair = models.BooleanField(
        default=False,
        verbose_name='С детским креслом или нет'
    )
    tariff = models.ForeignKey(
        to='tariffs.Tariff',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='orders',
        verbose_name='Тариф'
    )
    # price = models.DecimalField(  # !
    #     blank=True,
    #     null=True,
    #     max_digits=10,
    #     decimal_places=2,
    #     verbose_name='Цена поездки'
    # )
    price = models.PositiveIntegerField(  # !
        blank=True,
        # null=True,
        default=0,
        verbose_name='Цена поездки'
    )
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICE,
        default=NEW,
        verbose_name='Статус заказа'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Заказ создан'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Заказ обнавлён'
    )

    # обязательно проверь, MinValueValidator начинается от 0 включительно или нет
    # с MaxValueValidator тоже проверь начинается от 0 включительно или нет
    discount_percent = models.IntegerField(  # поле под вопросом
        default=0,
        validators=(
            MinValueValidator(0, message='Скидка не может быть меньше 0%'),
            MaxValueValidator(100, message='Скидка не может быть больше 100%'),
        ),
        verbose_name='Процент скидки'
    )

    def save(self, *args, **kwargs):
        """
            Установка окончательной цены невозможна в api
            ею можно воспользоваться через админку
            надо узнать, нужно ли гале это, или она всегда хочет устанавливать
            цену вручную, чтобы не было путаницы
        """
        if self.price == 0:
            if self.tariff and self.tariff.price_per_km:
                self.price = int(self.distance) * int(self.tariff.price_per_km)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created', '-departure_time',)


"""
Orders
    from_place - из какого города (VARCHAR)
    to_place - в какой город (VARCHAR)
    distance - сколько нужно проехать водителю
    departure - время отправления (datetime)
    driver - внешник ключ на таблицу с водителями
    car_class - внешние ключ на класс автомобиля
    client - имя клиента (или если всё таки у нас будет отдельная табл. для клиентов, то внешний ключ на эту таблицу)
    contact - контакты клиента
    remark - особые пометки, типа детского кресла
    price - цена
    status - 4 разных варианта (cancelled, new, read, ready_to_be, in_process, completed)
    created - когда создан заказ
    updated - последнее изменение заказа (?)
    discount - внешний ключ на таблицу Discount, может быть NULL
    discount_percent - процент скидки, под очень болшьшим вопросом.

Надо подумать, есть ли смысл создавать отдельную таблицу для
клиентов, и привязывать её к таблице по связи один ко многим
Можно создать отдельную таблицу для постоянных клиентов. 
Но при этом поле client и contact в таблице orders должно быть для новых клиентов, котрых большинство

Понятно, что таблица orders для заказов.
Детское кресло под вопросом. Возможно будет таблица с водителем,
и тогда придётся выносить детское кресло в отдельное поле
Но поле remark в любом случае должно быть (особые примечания к заказу)
"""
