from random import choices

from django.shortcuts import render
from django.template.context_processors import request
from django.core.paginator import Paginator
from .models import Transistor
from .forms import TransistorAdd

# Create your views here.
def index_app(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'app/main.html', context=context)


def transistor_app(request):
    SELECT_CHOUIS = ['5', '10', '15', '20', '25',]
    data = Transistor.objects.all()

    if request.GET.get('pag') is None:
        pag = 5
    else:
        pag = request.GET.get('pag')

    if request.method == 'POST':
        select = request.POST.get('select')
        if select is None:
            pag = 5
        else:
            pag = select

    paginator = Paginator(data, pag)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Транзисторы',
        'page_obj': page_obj,
        'select_chouis': SELECT_CHOUIS,
        'pag': pag,
    }
    return render(request, 'app/transistor.html', context=context)


def transistor_app_id(request, id_tr):
    data = Transistor.objects.get(id=id_tr)

    context = {
        'title': 'Транзистор',
        'data': data,
    }
    return render(request, 'app/transistor_id.html', context=context)


def transistor_forma_add(request):
    global form
    if request.method == 'POST' and request.FILES['path_file']:
        form = TransistorAdd(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            type_tr = form.cleaned_data['tpe_tr']
            korpus = form.cleaned_data['korpus']
            descr = form.cleaned_data['descr']
            path_file = form.cleaned_data['path_file']

            print(name)
            print(descr)
            print(path_file)
    else:
        form = TransistorAdd()


    data = {
        'title': 'Добаление транзистора в каталог',
        'form': form,
    }
    return render(request, 'app/transistor_forma_add2.html', context=data)