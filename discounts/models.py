from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

"""
Discounts

Таблица для рекламы
Где-то на сайте будет баннер со специальными акциями
Типо "скидка участникам СВО"
Размещаешь этот банер. Покупаешь рекламу в группе аля "Два майора".
PROFIT

Возможно нужно создать предпосылку для продажи рекламы на сайте,
Но пока об этом очень рано говорить

"""


class Discounts(models.Model):
    banner = models.CharField(
        max_length=255,
        verbose_name='Содержимое баннера'
    )
    valid_from = models.DateTimeField(
        verbose_name='Активен с какого числа'
    )
    valid_to = models.DateTimeField(
        verbose_name='Активен до какого числа'
    )
    discount = models.IntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(100)
        ),
        verbose_name='Скидка'
    )
    active = models.BooleanField(
        default=False,
        verbose_name='Активен',
    )

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

    def __str__(self):
        return f'{self.banner[:25]} (active - {self.active}, discount - {self.discount}%)'
