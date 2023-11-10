from django.contrib import admin

from feedback.models import (FeedBack, Review, )


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    # list_display = ('', )
    list_filter = ('read', )
    # search_fields = ('name', 'car',)  # 'author__username'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # list_display = ('',)
    list_filter = ('publish', )
    # search_fields = ('name', 'car',)  # 'author__username'

"""
from django.db import models


class FeedBack(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name='Имя отправителя'
    )
    phone_number = models.CharField(  # скорее можно убрать, зависит от формы на фронте
        max_length=25,
        default='',
        verbose_name='Телефонный номер'
    )
    email = models.CharField(
        max_length=60,
        default='',
        verbose_name='email'
    )
    message = models.TextField(
        max_length=500,
        verbose_name='Обращение'
    )
    read = models.BooleanField(
        default=False,
        verbose_name='Прочитан'
    )

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ('read',)

    def __str__(self):
        if self.read:
            read = 'Прочинат'
        else:
            read = 'НЕ прочитан'
        return f'{self.pk}) {read}'


class Review(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name='Имя отправителя'
    )
    message = models.TextField(
        max_length=500,
        verbose_name='Отзыв'
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    draft = models.BooleanField(
        default=False,
        verbose_name='Допустим к публикации'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('draft', '-date',)

    def __str__(self):
        if self.draft:
            moderate = 'прошёл модерацию'
        else:
            moderate = 'НЕ прошёл модерацию'
        return f'{self.pk}) {self.date} ({moderate})'

"""