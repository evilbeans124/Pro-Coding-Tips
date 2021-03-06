# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0004_auto_20160629_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('totalTips', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='tip',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tip',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tip',
            name='author',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='tip',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AddField(
            model_name='tip',
            name='series',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tips.Series'),
            preserve_default=False,
        ),
    ]
