# Generated by Django 3.2.11 on 2022-01-28 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CA', '0017_auto_20220128_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casignup',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 12, 11, 14, 32, 405781)),
        ),
        migrations.AlterField(
            model_name='prsignup',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 12, 11, 14, 32, 406060)),
        ),
    ]
