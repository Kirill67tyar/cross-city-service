from django.contrib import admin

from orders.models import Order

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
    
    from_place = models.CharField
    to_place = models.CharField
    # # travel_time - скорее всего не нужон
    # travel_time = models.PositiveSmallIntegerField(  # ? от 0 до 32767 (под большим вопросом, нужно ли)
    #     blank=True,
    #     null=True,
    #     verbose_name='Время в пути'
    # )
    distance = models.PositiveSmallIntegerField
    departure_time = models.DateTimeField
    driver = models.ForeignKey(  # внешний ключ на таблицу Drivers
        blank=True,
        null=True,
        to='drivers.Driver',
        on_delete=models.SET_NULL,
        related_name='orders',
        verbose_name='Водитель'
    )
    client = models.CharField
    contact = models.CharField
    remark = models.CharField(  # TextField
        # нужно для особых пометок:
        #  - перевоз инвалида
        #  - > 1 детского кресла
        #  - нестандартные средства связи
        #  - этничность водителя
        max_length=255,
        verbose_name='Примечания к заказу'
    )
    baby_chair = models.BooleanField
    tariff = models.ForeignKey(
        to='tariffs.Tariff',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='orders',
        verbose_name='Тариф'
    )
    price = models.PositiveIntegerField
    )
    status = models.CharField
    created = models.DateTimeField
    updated = models.DateTimeField
    discount_percent = models.IntegerField
"""


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('to_place', 'from_place', 'created', 'status',)
    list_filter = ('status',)
    search_fields = ('status', 'from_place', 'to_place', 'client', 'contact', 'remark',)
    # raw_id_fields = ('author',)  # благодаря этому атрибуту, появилась возможость искать автора не из списка
    # date_hierarchy = 'publish'  # ссылки для навигации по датам (под поиском)
    ordering = ('-created', '-departure_time',)
