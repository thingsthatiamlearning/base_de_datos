# Generated by Django 4.0.5 on 2022-07-07 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='url',
            field=models.URLField(blank=True, verbose_name='Enlace'),
        ),
    ]
