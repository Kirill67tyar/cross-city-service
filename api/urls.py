from django.urls import path

from api.views import (
    set_cookie_view,
    TariffAPIView,
    ContactAPIView,
    OrderCreateAPIView,
    ReviewListCreateAPIView,
    FeedbackCreateAPIView,
    cities_list_view,
)

app_name = 'api'

urlpatterns = [
    path('tariffs/list/', TariffAPIView.as_view(), name='tariffs-list'),
    path('orders/create/', OrderCreateAPIView.as_view(), name='orders-create'),
    path('reviews/create/', ReviewListCreateAPIView.as_view(), name='reviews-create'),
    path('reviews/list/', ReviewListCreateAPIView.as_view(), name='reviews-list'),
    path('feedback/create/', FeedbackCreateAPIView.as_view(), name='feedback-create'),
    path('cities/list/', cities_list_view, name='cities-list'),
    path('contacts/detail/<int:pk>/', ContactAPIView.as_view(), name='contacts-detail'),
    path('get-csrf-token/', set_cookie_view, name='set-cookie-csrf'),
]
