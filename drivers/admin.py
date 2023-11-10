from django.contrib import admin

from drivers.models import Driver

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

pk = BigAutoField
name = models.CharField
contact = models.CharField
car = models.CharField
tariff = models.ForeignKey(
    blank=True,
    null=True,
    to='tariffs.Tariff',
    on_delete=models.SET_NULL,
    related_name='drivers',
    verbose_name='Тариф'
)
"""

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'car',)
    # list_filter = ('', '', '', '',)
    search_fields = ('name', 'car',)  # 'author__username'
    ordering = ('name',)


