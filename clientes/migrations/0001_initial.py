# Generated by Django 4.0.5 on 2022-06-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('correoElectronico', models.EmailField(max_length=200, verbose_name='Correo')),
                ('numeroTelefonico', models.IntegerField(max_length=10, verbose_name='Telefono')),
                ('vivienda', models.CharField(max_length=100, verbose_name='LugarDondeVive')),
                ('nota', models.TextField(verbose_name='nota')),
            ],
        ),
    ]