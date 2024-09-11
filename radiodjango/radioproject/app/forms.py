from random import choices
from django.forms import ModelForm
from django import forms
from .models import Transistor


class TransistorAdd(ModelForm):
    class Meta:
        model = Transistor
        fields = ["name", "type", "korpus", "descr", "path_file"]
