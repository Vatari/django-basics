import time

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse(f"Response from {time.time()}")


def index2(request, *args, **kwargs):
    return HttpResponse(f"Response form {args} and {kwargs}")


def department_details(request, pk):
    return HttpResponse(f"Department ID {pk}")


def department_details_by_name(request, name):
    return HttpResponse(f"Department name {name}")


def department_list(request):
    pass


def departments_create(request):
    pass


