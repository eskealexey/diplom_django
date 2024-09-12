from random import choices

from django.shortcuts import render, redirect
# from django.template.context_processors import request
from django.core.paginator import Paginator
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
from urllib3 import HTTPResponse

from .models import Transistor
from .forms import TransistorAdd


def index_app(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'app/main.html', context=context)


def transistor_app(request):
    SELECT_CHOUIS = ['5', '10', '15', '20', '25', ]
    data = Transistor.objects.filter(userid=request.user.pk)

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
    if (request.POST):
        error = ''
        data_dict =  request.POST.dict()
        act = data_dict.get('act')
        quantity = data_dict.get('quantity ')
        try:
            quantity = abs(int(quantity))
            total = data.amount
            print(total)
            if act is not None:
                if act == 'add':
                    total += quantity
                elif (act == 'del') and (total >= quantity):
                    total -= quantity
                else:
                    error = 'удаляется больше чем есть'

                data.amount = total
                data.save(update_fields=['amount'])
            else:
                error = 'не выбрано действие'

            context = {
                'title': 'Транзистор',
                'data': data,
                'error': error,
            }
        except Exception as err:
            print(err)
            error = 'не число'
            context = {
                'title': 'Транзистор',
                'data': data,
                'error': error,
            }
        return render(request, 'app/transistor_id.html', context=context)
    else:
        context = {
            'title': 'Транзистор',
            'data': data,
            'error': '',
        }
        return render(request, 'app/transistor_id.html', context=context)


def transistor_forma_add(request):
    if request.method == 'POST':
        form = TransistorAdd(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            type_tr = form.cleaned_data['type']
            korpus = form.cleaned_data['korpus']
            descr = form.cleaned_data['descr']
            path_file = form.cleaned_data['path_file']
            form.save()
            Transistor.objects.filter(name=name).update(userid=request.user.pk)
            return redirect('transistorlist')
    else:
        form = TransistorAdd()
    data = {
        'title': 'Добаление транзистора в каталог',
        'form': form,
    }
    return render(request, 'app/transistor_forma_add2.html', context=data)



def found(request):
    if request.method == "GET":
        str_ = request.GET.get('find')
        data = Transistor.objects.filter(userid=request.user.pk, name__contains=str_).values()

    context = {
        'title': 'Поиск по наименованию',
        'data': data,
    }
    return render(request, 'app/transistorfound.html',context=context)