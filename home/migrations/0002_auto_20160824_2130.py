# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-25 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='descripcion_corta',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='slider',
            name='link',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='slider',
            name='titulo_link',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
