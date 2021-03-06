# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 03:51
from __future__ import unicode_literals

import blog.fields
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20160803_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=blog.fields.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator]),
        ),
        migrations.AlterField(
            model_name='zipcode',
            name='zipcode',
            field=models.CharField(help_text="'-'를 빼고 입력해주세요.", max_length=7, validators=[blog.validators.ZipcodeValidator(True)]),
        ),
    ]
