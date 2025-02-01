from django.shortcuts import render

# Create your views here.


def hellotask(request):
    return render(request, 'tasks.html')
