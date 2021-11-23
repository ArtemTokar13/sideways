# Generated by Django 3.2.9 on 2021-11-22 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChairModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(default='Estación de Carga', max_length=255)),
                ('estado', models.CharField(default='Libre', max_length=255)),
                ('destino', models.CharField(default='"En blanco"', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DepartamentoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=255)),
            ],
        ),
    ]
