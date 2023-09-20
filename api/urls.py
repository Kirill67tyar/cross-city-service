from django.urls import path

from api.views import (
    TariffAPIView,
    ContactAPIView,
    OrderCreateAPIView,
)

app_name = 'api'

urlpatterns = [
    path('tariffs/list/', TariffAPIView.as_view(), name='tariffs-list'),
    path('orders/create/', OrderCreateAPIView.as_view(), name='orders-create'),
    path('contacts/detail/<int:pk>/', ContactAPIView.as_view(), name='contacts-detail'),
]
