# Generated by Django 3.2.11 on 2022-01-27 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share2', '0006_auto_20220127_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='ipaddress',
            field=models.CharField(default='', max_length=350),
        ),
    ]