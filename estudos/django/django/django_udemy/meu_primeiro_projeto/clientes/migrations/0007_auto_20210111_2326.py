# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-01-11 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_telefone_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=14)),
                ('data_exp', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.CPF'),
            preserve_default=False,
        ),
    ]
