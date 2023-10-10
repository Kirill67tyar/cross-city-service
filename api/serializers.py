from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (CharField, ModelSerializer, )

from tariffs.models import Tariff
from staff.models import Contact
from orders.models import Order


class TariffListSerializer(ModelSerializer):
    quantity_seats_display = CharField(
        source='get_quantity_seats_display',
        read_only=True
    )

    # quantity_seats_ids = SerializerMethodField(read_only=True)
    #
    # def get_quantity_seats_ids(self, obj):
    #     return obj.pk

    # get_author работает здесь в связке с SerializerMethodField.
    # синтаксис следующий get_<name_field_in_db>, т.е. к get_добавдяем имя, которое мы хотим использовать как поле
    # благодаря SerializerMethodField мы делаем это поле только для чтения.
    # А благодаря get_author - выбираем то выводить в json файле в поле author
    # Но в данном случае они работают только в связке, по одному не могут (почему - не знаю)
    # Запомни эту связку - очень полезная штука.

    class Meta:
        model = Tariff
        fields = ['id', 'car_class', 'quantity_seats_display', 'price_per_km', ]  # 'price_per_km',
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'car_class': {
                'read_only': True
            },
            ## price_per_km - нужно отдавать в том случае, если нужно выводить цену за км. на сайте
            ## в идеале сделать так, чтобы фронт работал в обоих вариантах.
            'price_per_km': {
                'read_only': True
            },
        }


"""
    from_place = models.CharField
    to_place = models.CharField
    distance = models.PositiveSmallIntegerField
    departure_time = models.DateTimeField
    client = models.CharField
    contact = models.CharField
    remark = models.CharField
    baby_chair = models.BooleanField
    tariff = models.ForeignKey(
        to='tariffs.Tariff',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='orders',
        verbose_name='Тариф'
    )
    status = models.CharField
        choices=STATUS_CHOICE,
        default=NEW
    )

{
    "from_place": "Лобня",
    "to_place": "Икша",
    "departure_time": "2023-09-17T20:04",
    "client": "Ден",
    "contact": "1488",
    "baby_chair": false,
    "tariff": 4
}

"""


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'from_place',
            'to_place',
            'departure_time',  # YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]
            'client',
            'contact',
            'baby_chair',
            'tariff',
            'created',
        ]
        # extra_kwargs = {
        #     'from_place': {
        #         'write_only': True
        #     },
        #     'to_place': {
        #         'write_only': True,
        #     },
        #     'departure_time': {
        #         'write_only': True
        #     },
        #     'client': {
        #         'write_only': True
        #     },
        #     'contact': {
        #         'write_only': True,
        #     },
        #     'baby_chair': {
        #         'write_only': True
        #     },
        #     'tariff': {
        #         'write_only': True,
        #     },
        #     'status': {
        #         'write_only': True
        #     },
        # }


"""
class Contact(models.Model):
    phone = models.CharField
    whatsapp = models.CharField
    telegram = models.CharField
"""


class ContactDetailSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'phone',
            'whatsapp',
            'telegram',
        ]
        extra_kwargs = {
            'phone': {
                'read_only': True
            },
            'whatsapp': {
                'read_only': True
            },
            'telegram': {
                'read_only': True,
            },
        }
