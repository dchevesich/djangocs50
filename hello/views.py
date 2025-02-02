from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

lista_generica = ["hola", "hello", "bye"]


def hello(request):

    return render(request, 'base.html', {
        'lista': lista_generica
    })


def add(request):
    if request.method == "POST":
        tarea = request.POST.get('task')
        lista_generica.append(tarea)
        return redirect('hello')
    else:
        return render(request, 'add.html')
