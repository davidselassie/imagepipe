# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagepipe', '0004_auto_20160607_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mashup',
            name='image_file',
            field=models.ImageField(upload_to='mashups'),
        ),
        migrations.AlterField(
            model_name='source',
            name='image_file',
            field=models.ImageField(upload_to='sources'),
        ),
    ]
