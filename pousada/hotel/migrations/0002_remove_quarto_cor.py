# Generated by Django 2.2 on 2019-07-23 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quarto',
            name='cor',
        ),
    ]