# Generated by Django 3.2.9 on 2021-11-24 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chair', '0002_chairmodel_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairmodel',
            name='ubicacion',
            field=models.ForeignKey(default='Estacion de carga', on_delete=django.db.models.deletion.CASCADE, to='chair.departamentomodel'),
        ),
    ]
