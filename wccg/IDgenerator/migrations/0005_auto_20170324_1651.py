# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IDgenerator', '0004_auto_20170324_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rider',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]