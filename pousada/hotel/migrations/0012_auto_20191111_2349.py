# Generated by Django 2.2 on 2019-11-12 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_auto_20191111_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='checkin',
            field=models.DateTimeField(help_text='Preencha primeiro a data de entrada.', verbose_name='Entrada'),
        ),
    ]
