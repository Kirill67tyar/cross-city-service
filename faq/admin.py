from django.contrib import admin

from faq.models import (
    Topic, Question,
)

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
    
    
class Topic(models.Model):
    name = models.CharField
    slug = models.SlugField


class Question(models.Model):
    ANSWERED = 1
    NOT_ANSWERED = 0
    STATUS_CHOICES = (
        (ANSWERED, 'Отвечен'),
        (NOT_ANSWERED, 'Не отвечен'),
    )

    text_question = models.TextField
    answer = models.TextField
    topic = models.ForeignKey(
        to='Topic',
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Тема'
    )

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=NOT_ANSWERED,
        verbose_name='Статус'
    )
"""


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    search_fields = ('pk', 'name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}  # поле которое автоматически преобразует slug в title
    # raw_id_fields = ('author',)  # благодаря этому атрибуту, появилась возможость искать автора не из списка


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'topic', 'status', )
    list_filter = ('topic', 'status', )
    search_fields = ('text_question', 'answer',)
    # raw_id_fields = ('author',)  # благодаря этому атрибуту, появилась возможость искать автора не из списка
    ordering = ('status',)
