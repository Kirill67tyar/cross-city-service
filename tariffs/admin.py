from django.contrib import admin

from tariffs.models import Tariff


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    fields = (
        'car_class', 'quantity_seats', 'price_per_km', 'photo', 'sequence',
    )
    list_display = (
        'car_class', 'quantity_seats', 'price_per_km',
    )
    list_filter = (
        'car_class', 'quantity_seats',
    )
    search_fields = (
        'car_class', 'quantity_seats',
    )

    # raw_id_fields = ('author',)  # благодаря этому атрибуту, появилась возможость искать автора не из списка
    # date_hierarchy = 'publish'  # ссылки для навигации по датам (под поиском)
