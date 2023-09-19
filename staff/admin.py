from django.contrib import admin
from staff.models import Contact

"""
class Contact(models.Model):
    phone = models.CharField(
        max_length=12,
        verbose_name='Телефонный номер'
    )
    whatsapp = models.CharField(
        max_length=15,
        verbose_name='Whatsapp'
    )
    telegram = models.CharField(
        max_length=15,
        verbose_name='Telegram'
    )
"""


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'whatsapp', 'telegram',)
