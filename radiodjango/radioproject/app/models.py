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
    name = models.CharField(max_length=10)
    type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
    )
    korpus = models.CharField(
        max_length=8,
        choices=KORPUS_CHOICES,
        default='TO-92'
    )
    descr = models.TextField(default='Описание')
    amount = models.IntegerField(default=0)
    path_file =  models.FileField(upload_to='files/', null=True)

    def __str__(self):
        return self.name
