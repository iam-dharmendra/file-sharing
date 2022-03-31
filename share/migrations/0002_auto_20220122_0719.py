# Generated by Django 3.2.11 on 2022-01-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='received_From',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='recieved_file',
            field=models.FileField(blank=True, upload_to='received/'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/file'),
        ),
    ]