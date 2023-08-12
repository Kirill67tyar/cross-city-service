from django.shortcuts import render


def map_example(request):
    return render(request,
                  template_name='orders/map_example.html',
                  context={})
