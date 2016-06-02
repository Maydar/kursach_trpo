# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Заголовок'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
    ]