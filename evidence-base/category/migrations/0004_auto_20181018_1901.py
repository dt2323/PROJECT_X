# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-18 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_category_attribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=150),
        ),
    ]
