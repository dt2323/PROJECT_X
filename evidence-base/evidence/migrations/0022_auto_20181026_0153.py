# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-26 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evidence', '0021_auto_20181022_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='content_rating_1',
            field=models.CharField(blank=True, default='0', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='content_rating_2',
            field=models.CharField(blank=True, choices=[('0', 'No Input'), ('1', 'Very Weak'), ('2', 'Weak'), ('3', 'Moderate'), ('4', 'Strong'), ('5', 'Very Strong')], default='0', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='content_rating_3',
            field=models.CharField(blank=True, choices=[('0', 'No Input'), ('1', 'Very Weak'), ('2', 'Weak'), ('3', 'Moderate'), ('4', 'Strong'), ('5', 'Very Strong')], default='0', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='content_rating_4',
            field=models.CharField(blank=True, choices=[('0', 'No Input'), ('1', 'Very Weak'), ('2', 'Weak'), ('3', 'Moderate'), ('4', 'Strong'), ('5', 'Very Strong')], default='0', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='content_rating_5',
            field=models.CharField(blank=True, choices=[('0', 'No Input'), ('1', 'Very Weak'), ('2', 'Weak'), ('3', 'Moderate'), ('4', 'Strong'), ('5', 'Very Strong')], default='0', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='source_rating_1',
            field=models.CharField(blank=True, choices=[('0', 'No Input'), ('1', 'Very Weak'), ('2', 'Weak'), ('3', 'Moderate'), ('4', 'Strong'), ('5', 'Very Strong')], default='0', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='source_rating_2',
            field=models.CharField(blank=True, choices=[('0', 'No Input'), ('1', 'Very Weak'), ('2', 'Weak'), ('3', 'Moderate'), ('4', 'Strong'), ('5', 'Very Strong')], default='0', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='source_rating_3',
            field=models.CharField(blank=True, choices=[('0', 'No Input'), ('1', 'Very Weak'), ('2', 'Weak'), ('3', 'Moderate'), ('4', 'Strong'), ('5', 'Very Strong')], default='0', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='source_rating_4',
            field=models.CharField(blank=True, choices=[('0', 'No Input'), ('1', 'Very Weak'), ('2', 'Weak'), ('3', 'Moderate'), ('4', 'Strong'), ('5', 'Very Strong')], default='0', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='source_rating_5',
            field=models.CharField(blank=True, choices=[('0', 'No Input'), ('1', 'Very Weak'), ('2', 'Weak'), ('3', 'Moderate'), ('4', 'Strong'), ('5', 'Very Strong')], default='0', max_length=1, null=True),
        ),
    ]
