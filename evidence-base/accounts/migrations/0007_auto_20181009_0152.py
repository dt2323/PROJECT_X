# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-09 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20181009_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='User.username', unique=True),
        ),
    ]