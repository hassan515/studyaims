# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-18 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyAims', '0014_auto_20180118_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentcompanyinfo',
            name='agent_state',
            field=models.CharField(choices=[('Province', 'Province'), ('Punjab', 'Punjab'), ('Islamabad ICT', 'Islamabad ICT'), ('Sindh', 'Sindh'), ('KPC', 'KPC'), ('Balochistan', 'Balochistan'), ('Gilgit Baltistan', 'Gilgit Baltistan'), ('Azad Jamui Kashmir', 'Azad Jamui Kashmir')], default=(('Province', 'Province'), ('Punjab', 'Punjab'), ('Islamabad ICT', 'Islamabad ICT'), ('Sindh', 'Sindh'), ('KPC', 'KPC'), ('Balochistan', 'Balochistan'), ('Gilgit Baltistan', 'Gilgit Baltistan'), ('Azad Jamui Kashmir', 'Azad Jamui Kashmir')), max_length=500),
        ),
    ]
