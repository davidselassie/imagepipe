# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 22:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mashup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('mashup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='imagepipe.Mashup')),
            ],
        ),
    ]