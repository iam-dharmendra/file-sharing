# Generated by Django 4.0.1 on 2022-01-19 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CA', '0004_signup_link'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signUp',
            new_name='CasignUp',
        ),
        migrations.CreateModel(
            name='PrsignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('number', models.PositiveIntegerField()),
                ('password', models.CharField(default='', max_length=15)),
                ('confirmPassword', models.CharField(default='', max_length=15)),
                ('link', models.CharField(default='', max_length=55)),
                ('recommend_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CA.casignup')),
            ],
        ),
    ]
