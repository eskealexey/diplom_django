# Generated by Django 4.1.3 on 2024-09-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_transistor_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transistor',
            name='path_file',
            field=models.FilePathField(),
        ),
    ]
