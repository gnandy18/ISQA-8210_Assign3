# Generated by Django 3.2.6 on 2021-10-11 02:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_auto_20210827_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 21, 8, 53, 25224)),
        ),
    ]
