# Generated by Django 3.2.11 on 2022-01-24 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CA', '0009_auto_20220122_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casignup',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 8, 5, 0, 25, 281163)),
        ),
        migrations.AlterField(
            model_name='prsignup',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 8, 5, 0, 25, 281500)),
        ),
    ]
