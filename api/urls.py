from django.urls import path

from api.views import (
    TariffAPIView,
    ContactAPIView,
    OrderCreateAPIView,
    CitiesAPIView,
    cities_list_view,
    reserve_cities_list_view,
)

app_name = 'api'

urlpatterns = [
    path('tariffs/list/', TariffAPIView.as_view(), name='tariffs-list'),
    path('orders/create/', OrderCreateAPIView.as_view(), name='orders-create'),
    path('contacts/detail/<int:pk>/', ContactAPIView.as_view(), name='contacts-detail'),
    # path('cities/list/', CitiesAPIView.as_view(), name='cities-list'),
    path('cities/list/', cities_list_view, name='cities-list'),
    path('cities/list/reserve/', reserve_cities_list_view, name='cities-list-reserve'),
]
