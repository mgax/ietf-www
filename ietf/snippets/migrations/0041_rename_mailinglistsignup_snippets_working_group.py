# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-02-06 23:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0040_remove_mailinglistsignup_working_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailinglistsignup',
            old_name='snippets_working_group',
            new_name='working_group',
        ),
    ]
