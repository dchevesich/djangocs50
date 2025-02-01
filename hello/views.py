from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):

    lista_generica = ["hola", "hello", "bye"]

    return render(request, 'base.html', {
        'lista': lista_generica
    })
