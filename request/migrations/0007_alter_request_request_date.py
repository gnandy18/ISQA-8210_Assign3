# Generated by Django 3.2.6 on 2021-10-13 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0006_alter_request_request_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 13, 13, 51, 24, 243199)),
        ),
    ]
