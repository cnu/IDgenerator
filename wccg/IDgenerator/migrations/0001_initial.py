# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiderDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rider_id', models.CharField(db_index=True, max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.DateTimeField()),
                ('sex', models.CharField(max_length=6)),
                ('contact_number', models.CharField(db_index=True, max_length=15)),
                ('contact_email', models.CharField(max_length=50)),
                ('blood_group', models.CharField(max_length=20)),
                ('emergency_name', models.CharField(max_length=50)),
                ('emergency_number', models.CharField(max_length=15)),
                ('area', models.CharField(max_length=50)),
                ('address', models.TextField(null=True)),
                ('max_distance', models.IntegerField()),
                ('goals', models.TextField()),
                ('expectations', models.TextField()),
                ('event_types', models.TextField()),
                ('comments', models.TextField()),
            ],
            options={
                'db_table': 'rider_details',
            },
        ),
    ]
