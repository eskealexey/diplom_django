# from random import choices
#
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Transistor


class TransistorAdd(ModelForm):
    class Meta:
        model = Transistor
        fields = ["name", "markname", "type", "korpus", "descr", "path_file"]

class TransistorEdit(ModelForm):
    class Meta:
        model = Transistor
        fields = ["name", "markname", "type", "korpus", "descr", "path_file"]
