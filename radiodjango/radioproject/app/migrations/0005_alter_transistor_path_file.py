# Generated by Django 4.1.3 on 2024-09-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_transistor_path_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transistor',
            name='path_file',
            field=models.CharField(max_length=250),
        ),
    ]
