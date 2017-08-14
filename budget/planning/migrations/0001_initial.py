# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 21:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='MacroCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='macroCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planning.MacroCategory'),
        ),
    ]
