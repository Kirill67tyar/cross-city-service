from django.db import models


class Info(models.Model):
    """
    data - вся инфа о компании
    contacts - контакты
    main_telephone - контакты
    """


class Vacancy(models.Model):
    pass


class TypeVacancy(models.Model):
    pass


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
