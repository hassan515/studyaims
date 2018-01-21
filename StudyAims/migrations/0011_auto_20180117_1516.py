# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-17 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyAims', '0010_auto_20180117_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentcompanyinfo',
            name='language_classes',
            field=models.CharField(blank=True, default=None, max_length=400),
        ),
        migrations.AlterField(
            model_name='agentcompanyinfo',
            name='refusal_appeals',
            field=models.CharField(blank=True, choices=[('Refusal Appeals', 'Refusal Appeals'), ('Yes', 'Yes'), ('No', 'No')], default=(('Refusal Appeals', 'Refusal Appeals'), ('Yes', 'Yes'), ('No', 'No')), max_length=400),
        ),
    ]
