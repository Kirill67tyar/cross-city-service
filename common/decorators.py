from functools import wraps
from django.http import HttpResponseForbidden
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
)


def csrf_checking(func):
    @wraps(func)
    def dec(self, request, *args, **kwargs):
        if request.COOKIES.get('csrftoken') == request.data.pop('csrf_token', ''):
            return func(self, request, *args, **kwargs)
        else:
            return Response(status=HTTP_403_FORBIDDEN)  # пошлёт HTTP ответ с кодом 403 (forbidden)

    return dec
