# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-25 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0097_auto_20170925_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagebannerannouncement',
            name='date_inactive',
            field=models.DateTimeField(null=True),
        ),
    ]
