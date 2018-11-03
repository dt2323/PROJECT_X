# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-01 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20181101_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='content_rating_1_title',
            field=models.CharField(default='Content Characterstic 1', max_length=50),
        ),
        migrations.AddField(
            model_name='board',
            name='content_rating_1_weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='content_rating_2_title',
            field=models.CharField(default='Content Characterstic 2', max_length=50),
        ),
        migrations.AddField(
            model_name='board',
            name='content_rating_2_weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='content_rating_3_title',
            field=models.CharField(default='Content Characterstic 3', max_length=50),
        ),
        migrations.AddField(
            model_name='board',
            name='content_rating_3_weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='content_rating_4_title',
            field=models.CharField(default='Content Characterstic 4', max_length=50),
        ),
        migrations.AddField(
            model_name='board',
            name='content_rating_4_weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='content_rating_5_title',
            field=models.CharField(default='Content Characterstic 5', max_length=50),
        ),
        migrations.AddField(
            model_name='board',
            name='content_rating_5_weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='source_rating_1_title',
            field=models.CharField(default='Source Characterstic 1', max_length=50),
        ),
        migrations.AddField(
            model_name='board',
            name='source_rating_1_weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='source_rating_2_title',
            field=models.CharField(default='Source Characterstic 2', max_length=50),
        ),
        migrations.AddField(
            model_name='board',
            name='source_rating_2_weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='source_rating_3_title',
            field=models.CharField(default='Source Characterstic 3', max_length=50),
        ),
        migrations.AddField(
            model_name='board',
            name='source_rating_3_weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='source_rating_4_title',
            field=models.CharField(default='Source Characterstic 4', max_length=50),
        ),
        migrations.AddField(
            model_name='board',
            name='source_rating_4_weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='source_rating_5_title',
            field=models.CharField(default='Source Characterstic 5', max_length=50),
        ),
        migrations.AddField(
            model_name='board',
            name='source_rating_5_weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]