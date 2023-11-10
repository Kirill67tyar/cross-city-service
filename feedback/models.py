from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        query = super().get_queryset().filter(publish=True)
        return query


class FeedBack(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name='Имя отправителя'
    )
    phone_number = models.CharField(  # скорее можно убрать, зависит от формы на фронте
        max_length=25,
        default='',
        blank=True,
        verbose_name='Телефонный номер'
    )
    email = models.EmailField(
        max_length=60,
        default='',
        blank=True,
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
    timestamp = models.DateField(
        auto_now_add=True,
        verbose_name='Дата обращения'
    )

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ('read', '-timestamp',)

    def __str__(self):
        if self.read:
            read = 'Прочинат'
        else:
            read = 'НЕ прочитан'
        return f'{self.timestamp} - {read}'


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
    publish = models.BooleanField(
        default=False,
        verbose_name='Допустим к публикации'
    )
    # дополнительный менеджер объектов
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('publish', '-date',)

    def __str__(self):
        if self.publish:
            moderate = 'прошёл модерацию'
        else:
            moderate = 'НЕ прошёл модерацию'
        return f'{self.date} - {moderate}'
