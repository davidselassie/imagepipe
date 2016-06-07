# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imagepipe', '0002_auto_20160603_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='mashup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sources', to='imagepipe.Mashup'),
        ),
    ]