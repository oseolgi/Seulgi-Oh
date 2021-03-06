# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 02:23
from __future__ import unicode_literals

import blog.fields
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160728_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.CharField(max_length=100, validators=[blog.validators.ZipcodeValidator])),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=blog.fields.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator]),
        ),
    ]
