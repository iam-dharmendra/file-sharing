# Generated by Django 3.2.11 on 2022-01-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0003_alter_userdetails_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='recieved_file',
            field=models.FileField(blank=True, upload_to='media/received/'),
        ),
    ]
