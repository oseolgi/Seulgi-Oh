# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 11:42
from __future__ import unicode_literals

import blog.fields
import blog.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160801_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=blog.fields.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator]),
        ),
    ]
