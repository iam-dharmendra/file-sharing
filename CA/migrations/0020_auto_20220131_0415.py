# Generated by Django 3.2.11 on 2022-01-31 04:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CA', '0019_auto_20220128_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casignup',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 15, 4, 15, 22, 295410)),
        ),
        migrations.AlterField(
            model_name='prsignup',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 15, 4, 15, 22, 295729)),
        ),
    ]