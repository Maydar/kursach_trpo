# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160602_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='total_points',
            field=models.IntegerField(default=100, verbose_name='Макс. кол-во баллов'),
        ),
    ]
