# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
