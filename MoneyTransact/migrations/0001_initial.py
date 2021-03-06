# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-24 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('Rs', 'Rupees'), ('$', 'Dollar'), ('o/w', 'Others')], default='Rs', max_length=3)),
                ('Giver', models.CharField(max_length=50)),
                ('taker', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('reason', models.CharField(max_length=250)),
                ('place', models.CharField(max_length=50)),
            ],
        ),
    ]
