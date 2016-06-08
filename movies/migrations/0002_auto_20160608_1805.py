# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 18:05
from __future__ import unicode_literals
from django.db import migrations
from movie_database.worker_function import movie_data, rater_data, rating_data


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(movie_data),
        migrations.RunPython(rater_data),
        migrations.RunPython(rating_data)
    ]