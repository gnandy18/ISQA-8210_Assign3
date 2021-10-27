# Generated by Django 3.2.6 on 2021-10-13 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20211013_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='date',
        ),
        migrations.AddField(
            model_name='employees',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='employees',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]