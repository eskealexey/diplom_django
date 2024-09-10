from django.db import models

# Create your models here.
class Transistor(models.Model):
    TYPE_CHOICES = [
        ('TBN', 'Биполярный NPN'),
        ('TBP', 'Биполярный PNP'),
        ('TPN', 'Полевой N-канал'),
        ('TPP', 'Полевой P-канал'),
        ('OPT', 'Однопереходной'),
        ('NGB', 'Транзистор NGBT'),
    ]
    KORPUS_CHOICES = [
        ('TO-92', 'TO-92'),
        ('SOT-23', 'SOT-23'),
        ('SOT-89', 'SOT-89'),
        ('SOT-223', 'SOT-223'),
        ('TO-126', 'TO-126'),
        ('TO-220', 'TO-220'),
        ('TO-252', 'TO-252'),
        ('SOT-669', 'SOT-669'),
        ('TO-263', 'TO-263'),
    ]
    name = models.CharField(max_length=10, blank=False, unique=True, db_index=True, verbose_name='наименование')
    type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        verbose_name='тип транзистора',
    )
    korpus = models.CharField(
        max_length=20,
        choices=KORPUS_CHOICES,
        default='TO-92',
        verbose_name='тип корпуса',
    )
    descr = models.TextField(blank=True, verbose_name='краткое описание')
    amount = models.IntegerField(default=0, blank=True, verbose_name='количество, шт.')
    path_file = models.FileField(upload_to='datasheet', default=None, blank=True, verbose_name='datasheet')

    def __str__(self):
        return self.name

