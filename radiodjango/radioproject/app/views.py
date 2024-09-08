from random import choices

from django.shortcuts import render
from django.template.context_processors import request

from .models import Transistor

# Create your views here.
def index_app(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'app/index_template.html', context=context)


def transistor_app(request):
    data = Transistor.objects.all()
    # display_type = Transistor.objects.get(id=1)
    context = {
        'title': 'Транзисторы',
        'data': data,
    }
    return render(request, 'app/transistor.html', context=context)


def transistor_app_id(request, id_tr):
    data = Transistor.objects.get(id=id_tr)

    context = {
        'title': 'Транзистор',
        'data': data,
    }
    return render(request, 'app/transistor_id.html', context=context)