from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transistor(models.Model):
    name = models.CharField(max_length=10, blank=False, unique=True, db_index=True, verbose_name='наименование')
    markname = models.CharField(max_length=20, blank=True, verbose_name='маркировка')
    type = models.ForeignKey('TypeTransistor', on_delete=models.PROTECT, null=True, verbose_name='тип транзистора')
    korpus = models.ForeignKey('KorpusTransistor', on_delete=models.PROTECT, null=True, verbose_name='корпус')
    descr = models.TextField(blank=True, verbose_name='краткое описание')
    amount = models.IntegerField(default=0, blank=True, verbose_name='количество, шт.')
    path_file = models.FileField(upload_to='datasheet/transistors', default=None, blank=True, verbose_name='datasheet')

    def __str__(self):
        return self.name


class TypeTransistor(models.Model):
    type_tr = models.CharField(max_length=20, blank=False, unique=True, db_index=True, verbose_name='тип_транзистора')

    def __str__(self):
        return self.type_tr


class KorpusTransistor(models.Model):
    korpus_tr = models.CharField(max_length=8, blank=False, unique=True, db_index=True, verbose_name='тип_корпуса')

    def __str__(self):
        return self.korpus_tr

