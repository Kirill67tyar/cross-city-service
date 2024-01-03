from rest_framework.fields import SerializerMethodField, ListField, IntegerField
from rest_framework.serializers import (CharField, ModelSerializer, Serializer, )
from rest_framework import serializers

from cities.models import City
from orders.models import Order
from staff.models import Contact
from tariffs.models import Tariff
from feedback.models import (
    FeedBack, Review,
)


class TariffListSerializer(ModelSerializer):
    quantity_seats_display = CharField(
        source='get_quantity_seats_display',
        read_only=True
    )
    marks = serializers.SerializerMethodField(read_only=True)

    def get_marks(self, obj):  # obj - экземпляр Note
        if obj.marks:
            return obj.marks.split(', ')
        return []

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
        fields = [
            'id', 'car_class', 'quantity_seats_display', 'price_per_km', 'photo', 'marks',
        ]
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
            'photo': {
                'read_only': True
            },
        }


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
            # 'created',
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


class FeedBackCreateSerializer(ModelSerializer):
    # phone_number = serializers.CharField(max_length=25, required=False)
    # email = serializers.CharField(max_length=60, required=False)

    class Meta:
        model = FeedBack
        fields = [
            'name',
            'phone_number',
            'email',
            'message',
        ]
        extra_kwargs = {
            'phone_number': {
                'allow_blank': True,
            },
            'email': {
                'allow_blank': True,
            },
        }


class ReviewCreateSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'name',
            'date',
            'message',
        ]
        extra_kwargs = {
            'id': {
                'read_only': True
            },
        }
