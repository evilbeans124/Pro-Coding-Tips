# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0015_auto_20160629_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
