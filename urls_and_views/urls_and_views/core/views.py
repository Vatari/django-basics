from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404


# Create your views here.
def new_index(request, *args, **kwargs):

    context = {
        'title': 'Request data',
        'args': args,
        'kwargs': kwargs,
        'path': request.path,
        'method': request.method,
    }
    return render(request, 'core/index.html', context)
