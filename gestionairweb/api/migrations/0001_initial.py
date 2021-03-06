# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 16:15
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='unique alphanum id')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('location', models.CharField(max_length=250, verbose_name='location')),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(null=True, verbose_name='end date')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('code', models.CharField(max_length=250, primary_key=True, serialize=False, verbose_name='player event code')),
                ('json', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
