# Generated by Django 2.2 on 2019-11-12 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_auto_20191111_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='valor_diaria',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor diária'),
        ),
    ]