from django.urls import path

from orders.views import map_example

app_name = 'orders'

urlpatterns = [
    path('map-example/', map_example, name='map-example'),
]
