from random import choices

from django import forms


class TransistorAdd(forms.Form):
    TYPE_CHOICES = (
        ('TBN', 'Биполярный NPN'),
        ('TBP', 'Биполярный PNP'),
        ('TPN', 'Полевой N-канал'),
        ('TPP', 'Полевой P-канал'),
        ('OPT', 'Однопереходной'),
        ('NGB', 'Транзистор NGBT'),
    )
    KORPUS_CHOICES = (
        ('TO-92', 'TO-92'),
        ('SOT-23', 'SOT-23'),
        ('SOT-89', 'SOT-89'),
        ('SOT-223', 'SOT-223'),
        ('TO-126', 'TO-126'),
        ('TO-220', 'TO-220'),
        ('TO-252', 'TO-252'),
        ('SOT-669', 'SOT-669'),
        ('TO-263', 'TO-263'),
    )
    name = forms.CharField(max_length=10, label='Название:')
    type_tr = forms.ChoiceField(choices=TYPE_CHOICES, label='Тип транзистора:')
    korpus = forms.ChoiceField(choices=KORPUS_CHOICES, label='Тип корпуса:')
    descr = forms.CharField(widget=forms.Textarea, label='Краткое описание:')
    path_file = forms.FileField( )
