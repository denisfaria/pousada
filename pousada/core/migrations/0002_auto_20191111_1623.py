# Generated by Django 2.2 on 2019-11-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='receber',
            field=models.BooleanField(default=False),
        ),
    ]
