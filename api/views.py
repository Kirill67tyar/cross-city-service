from django.views.decorators.csrf import csrf_protect, requires_csrf_token
from django.utils.decorators import method_decorator
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
)
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
)

from orders.models import Order
from staff.models import Contact
from tariffs.models import Tariff
from api.serializers import (
    TariffListSerializer,
    OrderCreateSerializer,
    ContactDetailSerializer,
)


class TariffAPIView(ListAPIView):
    serializer_class = TariffListSerializer
    queryset = Tariff.objects.all()
    http_method_names = [
        'get',
        'options',
        'head',
    ]


# @method_decorator(csrf_protect, name='post')
# @method_decorator(requires_csrf_token, name='post')
class OrderCreateAPIView(ListCreateAPIView):  # ListCreateAPIView CreateAPIView
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()
    http_method_names = [
        'get',
        'post',
    ]


class ContactAPIView(RetrieveAPIView):
    serializer_class = ContactDetailSerializer
    queryset = Contact.objects.all()
    http_method_names = [
        'get',
        'options',
        'head',
    ]
