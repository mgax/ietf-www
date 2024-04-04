# Generated by Django 2.2.19 on 2021-11-01 01:13

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


def migrate_data(apps, schema_editor):
    SecondaryMenu = apps.get_model('utils', 'SecondaryMenu')
    ToolsMenuItem = apps.get_model('utils', 'ToolsMenuItem')
    MenuItem = apps.get_model('utils', 'MenuItem')
    SubMenuItem = apps.get_model('utils', 'SubMenuItem')
    menu = SecondaryMenu.objects.first()
    if menu is not None:
        contact_menu = MenuItem(page=menu.contact_page, sort_order=1)
        contact_menu.save()
        tools_menu = MenuItem(page=menu.tools_page, sort_order=2)
        tools_menu.save()

        for item in ToolsMenuItem.objects.all():
            sub_menu = SubMenuItem(parent=tools_menu, page=item.page, link=item.link, text=item.text)
            sub_menu.save()


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('text', models.CharField(blank=True, max_length=40)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubMenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link', models.URLField(blank=True)),
                ('text', models.CharField(blank=True, max_length=40)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('parent', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_menu_items', to='utils.MenuItem')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RunPython(migrate_data),
        migrations.RemoveField(
            model_name='toolsmenuitem',
            name='model',
        ),
        migrations.RemoveField(
            model_name='toolsmenuitem',
            name='page',
        ),
        migrations.DeleteModel(
            name='SecondaryMenu',
        ),
        migrations.DeleteModel(
            name='ToolsMenuItem',
        ),
    ]
