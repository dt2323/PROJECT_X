# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-18 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evidence', '0018_auto_20181015_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidence',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=150),
        ),
    ]