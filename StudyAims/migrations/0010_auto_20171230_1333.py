# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-30 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyAims', '0009_auto_20171230_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='stdpersonalinfo',
            name='experience2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='stdpersonalinfo',
            name='studyGap',
            field=models.CharField(choices=[('1990', '1990'), ('1991', '1991')], default=(('1990', '1990'), ('1991', '1991')), max_length=10),
        ),
        migrations.AlterField(
            model_name='stdpersonalinfo',
            name='experience',
            field=models.CharField(choices=[('1990', '1990'), ('1991', '1991')], default=(('1990', '1990'), ('1991', '1991')), max_length=10),
        ),
    ]
