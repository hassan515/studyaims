# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-12 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyAims', '0006_auto_20180112_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentcompanyinfo',
            name='scholarshipfee',
            field=models.CharField(blank=True, choices=[('Scholarship Fees', 'Scholarship Fees'), ('0-5000', '0-5000'), ('5000-10,000', '5000-10,000'), ('10,000-15000', '10,000-15000'), ('15000-20,000', '15000-20,000'), ('20,000-25000', '20,000-25000'), ('25000-30,000', '25000-30,000'), ('30,000-35000', '30,000-35000'), ('35000-40,000', '35000-40,000'), ('40,000-45000', '40,000-45000'), ('45000-50,000', '45000-50,000'), ('50,000-60,000', '50,000-60,000'), ('60,000-70,000', '60,000-70,000'), ('70,000-80,000', '70,000-80,000'), ('80,000-90,000', '80,000-90,000'), ('90,000-100,000', '90,000-100,000'), ('100,000-125,000', '100,000-125,000'), ('125,000-150,000', '125,000-150,000'), ('150,000-200,000', '150,000-200,000')], default=(('Scholarship Fees', 'Scholarship Fees'), ('0-5000', '0-5000'), ('5000-10,000', '5000-10,000'), ('10,000-15000', '10,000-15000'), ('15000-20,000', '15000-20,000'), ('20,000-25000', '20,000-25000'), ('25000-30,000', '25000-30,000'), ('30,000-35000', '30,000-35000'), ('35000-40,000', '35000-40,000'), ('40,000-45000', '40,000-45000'), ('45000-50,000', '45000-50,000'), ('50,000-60,000', '50,000-60,000'), ('60,000-70,000', '60,000-70,000'), ('70,000-80,000', '70,000-80,000'), ('80,000-90,000', '80,000-90,000'), ('90,000-100,000', '90,000-100,000'), ('100,000-125,000', '100,000-125,000'), ('125,000-150,000', '125,000-150,000'), ('150,000-200,000', '150,000-200,000')), max_length=400, null=True),
        ),
    ]
