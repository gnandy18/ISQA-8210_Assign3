# Generated by Django 3.2.6 on 2021-08-27 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='cat_type',
            new_name='category_type',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='loc_type',
            new_name='location_type',
        ),
    ]
