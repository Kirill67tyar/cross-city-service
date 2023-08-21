from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)


class Orders:
    STATUS_CHOICE = (
        ('new', 'New',),  # новый непрочитанный заказ
        ('read', 'Read',),  # прочитанный заказ (водитель не найден)
        ('ready_to_be', 'Ready_to_be',),  # заказ готов к исполнению (водитель найден)
        ('in_process', 'In_process',),  # заказ выполняется в данный момент
        ('completed', 'Completed',),  # заказ завершён
        ('cancelled', 'Cancelled',),  # заказ по какой-то причине отменён
    )
    from_place = models.CharField(
        max_length=100,
        verbose_name='Место отправления'
    )
    to_place = models.CharField(
        max_length=100,
        verbose_name='Место прибытия'
    )
    travel_time = models.PositiveSmallIntegerField(  # от 0 до 32767 (под большим вопросом, нужно ли)
        verbose_name='Время в пути'
    )
    distance = models.PositiveIntegerField(
        verbose_name='Дистанция в км.'
    )
    departure_time = models.DateTimeField(
        verbose_name='Время отправления'
    )
    driver = ...  # внешний ключ на таблицу Drivers
    car_class = ...  # внешний ключ на таблицу с классами машин
    client = models.CharField(
        max_length=100,
        verbose_name='Клиент'
    )
    contact = models.CharField(
        max_length=100,
        verbose_name='Телефон клиента'
    )
    remark = models.CharField(
        max_length=255,
        verbose_name='Примечания к заказу'
    )
    baby_chair = models.PositiveSmallIntegerField(max_length=15)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена поездки'
    )
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICE,
        default='new',
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
    discount = ...  # внешний ключ на таблицу Discount
    discount_percent = models.IntegerField(  # поле под вопросом
        default=0,
        validators=(
            MinValueValidator(0),
            MaxValueValidator(100),
        ),
        verbose_name='Процент скидки'
    )


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
