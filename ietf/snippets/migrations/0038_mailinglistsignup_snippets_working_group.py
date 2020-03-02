# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-02-06 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0037_populate_snippets_from_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailinglistsignup',
            name='snippets_working_group',
            field=models.ForeignKey(blank=True, help_text='The group whose mailing list sign up address should be used. If sign up is set then this does not need to be set.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.WorkingGroup'),
        ),
    ]
