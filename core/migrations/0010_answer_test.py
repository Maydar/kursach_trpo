# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_question_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Test', verbose_name='Тест'),
            preserve_default=False,
        ),
    ]