from functools import wraps
from django.http import HttpResponseForbidden


def csrf_checking(func):
    @wraps(func)
    def dec(self, request, *args, **kwargs):
        if request.COOKIES.get('csrftoken') == request.data.pop('csrf_token', ''):
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()  # пошлёт HTTP ответ с кодом 403 (forbidden)

    return dec
