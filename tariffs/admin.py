from django.contrib import admin

from tariffs.models import Tariff

"""
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'slug', 'category', 'available', 'price', 'created', 'updated',
    list_editable = 'available', 'price',
    list_filter = 'category', 'available', 'created', 'updated',
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('code',)
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'author', 'publish', 'status',)
    list_filter = ('publish', 'author', 'created', 'status',)
    search_fields = ('title', 'body', 'slug', 'author__username',)
    prepopulated_fields = {'slug': ('title',)}  # поле которое автоматически преобразует slug в title
    raw_id_fields = ('author',)  # благодаря этому атрибуту, появилась возможость искать автора не из списка
    date_hierarchy = 'publish'  # ссылки для навигации по датам (под поиском)
    ordering = ('status', 'publish',)
    
    car_class = models.CharField
    quantity_seats = models.CharField(
        choices=QUANTITY_SEATS_CHOICE,
    price_per_km = models.PositiveSmallIntegerField
"""


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    fields = ('car_class', 'quantity_seats', 'price_per_km', 'photo',)
    list_display = (
        'car_class', 'quantity_seats',
    )
    list_filter = (
        'car_class', 'quantity_seats',
    )
    search_fields = (
        'car_class', 'quantity_seats',
    )
    # raw_id_fields = ('author',)  # благодаря этому атрибуту, появилась возможость искать автора не из списка
    # date_hierarchy = 'publish'  # ссылки для навигации по датам (под поиском)
