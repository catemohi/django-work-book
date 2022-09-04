from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(reqests):
    return HttpResponse('Тестовая index.view')


def params_int(reqests, value):
    print(type(value))
    return HttpResponse(f'принят int параметр: {value}')

def params_slug(reqests, value):
    print(type(value))
    return HttpResponse(f'принят slug параметр: {value}')

def params_uuid(reqests, value):
    print(type(value))
    return HttpResponse(f'принят uuid параметр: {value}')

def params_str(reqests, value):
    print(type(value))
    return HttpResponse(f'принят str параметр: {value}')

def params_line(reqests, value):
    print(type(value))
    return HttpResponse(f'принят line параметр: {value}')

