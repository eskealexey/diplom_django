# Generated by Django 4.2.11 on 2024-09-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transistor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('type', models.CharField(choices=[('TBN', 'Биполярный NPN'), ('TBP', 'Биполярный PNP'), ('TPN', 'Полевой N-канал'), ('TPP', 'Полевой P-канал'), ('OPT', 'Однопереходной'), ('NGB', 'Транзистор NGBT')], max_length=3)),
                ('korpus', models.CharField(choices=[('TO-92', 'TO-92'), ('SOT-23', 'SOT-23'), ('SOT-89', 'SOT-89'), ('SOT-223', 'SOT-223'), ('TO-126', 'TO-126'), ('TO-220', 'TO-220'), ('TO-252', 'TO-252'), ('SOT-669', 'SOT-669'), ('TO-263', 'TO-263')], default='TO-92', max_length=8)),
                ('descr', models.TextField(default='Описание')),
                ('amount', models.IntegerField(default=0)),
                ('path_file', models.FileField(upload_to='')),
            ],
        ),
    ]
