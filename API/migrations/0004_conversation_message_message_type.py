# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_auto_20171014_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.User')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('response', models.BooleanField()),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Conversation')),
            ],
        ),
        migrations.CreateModel(
            name='Message_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Message')),
            ],
        ),
    ]
