# Generated by Django 4.0.1 on 2022-01-19 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CA', '0003_alter_signup_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='link',
            field=models.CharField(default='', max_length=55),
        ),
    ]
