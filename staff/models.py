from django.db import models

"""
    Эти таблицы стоит продумать более тщательно, чем сейчас
    Пока не знаю, как в них будут обновляться данные.
    Это просто примерный набросок.
    
    В чём суть.
    На странице сайта у нас будут средства связи: 
    - обычный телефон
    - whatsapp
    - telegram
    - почта (?)
    
    Надо продумать, как лучше доставать эти данные из
    бэкенда.
    Как сделать так, чтобы их легко можно было обновить при желании.
"""


#
# def contact_default():
#     return {
#         'email': '',
#         'numbers': [],
#         'tg_name_user': '',
#     }
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
    
    class Meta:
        verbose_name = 'Мои контакты'
        verbose_name_plural = 'Мои контакты'


#
# class Info(models.Model):
#     about_us = models.TextField(
#         verbose_name='Информация о сервисе'
#     )
#     contact_info = models.JSONField(
#         verbose_name='Контакты',
#         default=contact_default
#     )
#     main_telephone = models.CharField(
#         max_length=15,
#         verbose_name='Главный телефон'
#     )
#
#
class Vacancy(models.Model):
    position = models.CharField(
        max_length=100,
        verbose_name='Позиция'
    )
    requirements = models.TextField(
        verbose_name='Требования'
    )
    type_vacancy = models.ForeignKey(
        to='staff.TypeVacancy',
        on_delete=models.CASCADE,
        verbose_name='Тип вакансии',
        related_name='vacancies'
    )


class TypeVacancy(models.Model):
    type_vacancy = models.CharField(
        max_length=50,
        verbose_name='Тип вакансии'
    )


"""
 -----
Info
    data - вся инфа о компании
    contacts - контакты

Моделька для информации о компании
Здесь будет указана инфа о компании и телефон(ы) для связи
 -----

 -----
Vacancies
    vacancy - какая ваконсия требуется

TypesVacancies
    (типо водитель, оператор и т.д.)

Две модельки, в которых содержатся данные о вакансиях
Vacancies ссылается на TypesVacancies по внешнему ключу (многие к одному)
 -----


 -----
Faq

FaqAnswers

Модельки для с вопросами и ответами
Тут можно подумать, как это реализовать в виде таблиц
Пока предварительно создать две отдельные таблицы, и связать
Их поля по связи один к одному
 -----
"""
