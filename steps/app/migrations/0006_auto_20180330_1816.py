# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-30 12:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180330_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incubator',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='incubator_follows', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='incubator',
            name='incubated_startup',
            field=models.ManyToManyField(blank=True, related_name='incubators', through='app.IncubatorStartup', to='app.Startup'),
        ),
        migrations.AlterField(
            model_name='incubator',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='incubator_members', through='app.IncubatorMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='incubator',
            name='ratings',
            field=models.ManyToManyField(blank=True, related_name='rated_incubators', through='app.IncubatorRating', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='startup',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='startup_members', through='app.StartupMember', to=settings.AUTH_USER_MODEL),
        ),
    ]
