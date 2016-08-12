# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_name', models.CharField(max_length=100)),
                ('pokemon_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_id', models.CharField(max_length=100)),
                ('trainer_name', models.CharField(max_length=100)),
                ('trainer_regdate', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='capture',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemongo.Pokemon'),
        ),
        migrations.AddField(
            model_name='capture',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemongo.Trainer'),
        ),
    ]