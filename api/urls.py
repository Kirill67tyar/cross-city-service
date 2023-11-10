from django.urls import path

from api.views import (
    get_csrf_token,
    TariffAPIView,
    ContactAPIView,
    OrderCreateAPIView,
    ReviewCreateAPIView,
    FeedbackCreateAPIView,
    cities_list_view,
)

app_name = 'api'

urlpatterns = [
    path('tariffs/list/', TariffAPIView.as_view(), name='tariffs-list'),
    path('orders/create/', OrderCreateAPIView.as_view(), name='orders-create'),
    path('reviews/create/', ReviewCreateAPIView.as_view(), name='reviews-create'),
    path('feedback/create/', FeedbackCreateAPIView.as_view(), name='feedback-create'),
    path('cities/list/', cities_list_view, name='cities-list'),
    path('contacts/detail/<int:pk>/', ContactAPIView.as_view(), name='contacts-detail'),
    path('get-csrf-token/', get_csrf_token, name='get-csrf-token'),
]
