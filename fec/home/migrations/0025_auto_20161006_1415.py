# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-06 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_presslandingpage_feed_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressreleasepage',
            name='category',
            field=models.CharField(choices=[('audit reports', 'Audit reports'), ('campaign finance data summaries', 'Campaign finance data summaries'), ('commission appointments', 'Commission appointments'), ('disclosure initiatives', 'Disclosure initiatives'), ('enforcement matters', 'Enforcement matters'), ('hearings', 'Hearings'), ('litigation', 'Litigation'), ('non-filer publications', 'Non-filer publications'), ('open meetings and related matters', 'Open meetings and related matters'), ('presidential public funds', 'Presidential public funds'), ('rulemakings', 'Rulemakings'), ('other agency actions', 'Other agency actions'), ('', '')], max_length=255),
        ),
    ]
