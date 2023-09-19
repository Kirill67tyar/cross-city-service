from django.urls import path

from drivers.views import fixture_for_driver

app_name = 'drivers'

urlpatterns = [
    path('insert_db/', fixture_for_driver, name='insert-db'),
]