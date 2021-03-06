# Generated by Django 2.2 on 2019-07-22 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField()),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Padrao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=200)),
                ('cidade', models.CharField(blank=True, max_length=200, null=True)),
                ('endereco', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=7)),
                ('valor_diaria', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cor', models.CharField(max_length=15)),
                ('observacoes', models.TextField()),
                ('padrao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Padrao')),
            ],
        ),
        migrations.CreateModel(
            name='MovRotativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_diaria', models.DecimalField(decimal_places=2, help_text='Valor do quarto reservado.', max_digits=5)),
                ('checkin', models.DateTimeField()),
                ('checkout', models.DateTimeField(blank=True, null=True)),
                ('forma_pagto', models.CharField(choices=[('di', 'Dinheiro'), ('de', 'Débito'), ('cr', 'Crédito')], default='de', max_length=2, verbose_name='forma de pagto')),
                ('pago', models.BooleanField(default=False)),
                ('nome_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.Pessoa')),
                ('quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Quarto')),
            ],
        ),
        migrations.CreateModel(
            name='MovMensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_pgto', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('mensalista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Mensalista')),
            ],
        ),
        migrations.AddField(
            model_name='mensalista',
            name='quarto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Quarto'),
        ),
    ]
