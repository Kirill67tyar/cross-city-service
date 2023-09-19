import os.path
from pprint import pprint as pp
from random import randrange, choice
from russian_names import RussianNames

from django.db import DatabaseError
from django.http import HttpResponse
from django.shortcuts import render

from tariffs.models import Tariff
from drivers.models import Driver

"""    
    name 
    contact 
    car 
    tariff
    
('Эконом',)('Комфорт',)('Универсал',)('Комфорт+',)('Бизнес',)('Минивэн (менее 7 мест)',)
('Минивэн (более 7 мест)',)('Спринтер',)('Грузоперевозки',)


    """


def fixture_for_driver(request):
    if request.method == 'POST':
        rn = RussianNames(count=20, patronymic=False, name_reduction=True)
        names = rn.get_batch()
        names = ('КАМА ПУЛЯ', 'МАГА ЛЕЗГИН',) + names
        numbers = [
            '8' + ''.join([str(randrange(10)) for i in range(10)])
            for _ in range(20)
        ]
        numbers.insert(0, '81111111111')
        numbers.insert(0, '89999999999')

        with open(
                file='common/car_models.txt',
                mode='r'
        ) as f:
            storage = f.read().split('\n')
        cars = list(filter(bool, storage))
        car_storage = [[]]
        for car in storage:
            if not car:
                car_storage.append([])
            else:
                car_storage[-1].append(car)
        tariffs = list(Tariff.objects.all())

        tariffs = tariffs[:-1]
        tariffs_cars = list(zip(car_storage, tariffs))
        # pp(tariffs_cars)
        tariffs_storage = []
        for q, tar in tariffs_cars:
            for _ in range(len(q)):
                tariffs_storage.append(tar)
        # print('\n', len(tariffs_storage), sep='\n')
        # pp(tariffs_storage)
        data = list(map(list, zip(names, numbers, cars, tariffs_storage)))
        pp(data)
        pp(len(data))
        for record in data:
            v = Driver(
                name=record[0],
                contact=record[1],
                car=record[2],
                tariff=record[-1],
            )
            try:
                v.save()
            except DatabaseError:
                pass

    return render(
        request=request,
        template_name='drivers/insert_db.html',
        context={}
    )
