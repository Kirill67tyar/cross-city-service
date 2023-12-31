from pprint import pprint as pp

from django.http import (
    JsonResponse,
    HttpResponse,
    HttpResponseForbidden,
)
from django.middleware.csrf import get_token
from django.shortcuts import redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods

from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
)

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_403_FORBIDDEN,
)
from rest_framework.decorators import api_view

from cities.models import City
from orders.models import Order
from staff.models import Contact
from tariffs.models import Tariff
from feedback.models import (
    FeedBack, Review,
)
from api.serializers import (
    TariffListSerializer,
    OrderCreateSerializer,
    ReviewCreateSerializer,
    ContactDetailSerializer,
    FeedBackCreateSerializer,
)
from common.decorators import csrf_checking


class TariffAPIView(ListAPIView):
    serializer_class = TariffListSerializer
    queryset = Tariff.objects.all()
    http_method_names = [
        'get',
        'options',
        'head',
    ]


class OrderCreateAPIView(ListCreateAPIView):  # ListCreateAPIView CreateAPIView
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()
    http_method_names = [
        'get',
        'post',
    ]

    # @csrf_checking
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class FeedbackCreateAPIView(ListCreateAPIView):  # ListCreateAPIView CreateAPIView
    serializer_class = FeedBackCreateSerializer
    queryset = FeedBack.objects.all()
    http_method_names = [
        'get',
        'post',
    ]

    # @csrf_checking
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ReviewListCreateAPIView(ListCreateAPIView):  # ListCreateAPIView CreateAPIView
    serializer_class = ReviewCreateSerializer
    queryset = Review.published.all()
    http_method_names = [
        'get',
        'post',
    ]

    # @csrf_checking
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ContactAPIView(RetrieveAPIView):
    serializer_class = ContactDetailSerializer
    queryset = Contact.objects.all()
    http_method_names = [
        'get',
        'options',
        'head',
    ]


@require_http_methods(['GET', 'HEAD'])
def reserve_cities_list_view(request):
    if request.method == 'GET':
        cities = list(City.objects.values_list('name', flat=True))
        # json_data = json.dumps(cities, ensure_ascii=False)
        # response = HttpResponse(json_data, content_type='application/json', charset='utf-8')
        response = JsonResponse(cities, safe=False, json_dumps_params={'ensure_ascii': False})
        return response
    return JsonResponse({'error': 'forbidden method'})


@api_view(['GET', 'HEAD'])
def cities_list_view(request):
    cities = list(City.objects.values_list('name', flat=True))
    return Response(data=cities, status=HTTP_200_OK)


@require_http_methods(['GET', ])
@ensure_csrf_cookie
def set_cookie_view(request):
    csrf_token = request.COOKIES.get('csrftoken')
    if csrf_token:
        return JsonResponse(
            data={'csrf_token': csrf_token, },
            json_dumps_params={'ensure_ascii': False}
        )
    return JsonResponse(
        data={'Set-Cookie': True, },
        json_dumps_params={'ensure_ascii': False}
    )


# ----------------------------------------Эксперимантальные вьюхи для csrf
@require_http_methods(['GET', ])
def get_csrf_view(request):
    csrf_token = request.COOKIES.get('csrftoken')
    if csrf_token:
        return JsonResponse(
            data={'csrf_token': csrf_token, },
            json_dumps_params={'ensure_ascii': False}
        )
    return redirect('api:set-csrf')


@require_http_methods(['GET', ])
@ensure_csrf_cookie
def set_csrf_view(request):
    # или используй функцию get_token
    return JsonResponse(
        data={'Set-Cookie': True, },
        json_dumps_params={'ensure_ascii': False}
    )
