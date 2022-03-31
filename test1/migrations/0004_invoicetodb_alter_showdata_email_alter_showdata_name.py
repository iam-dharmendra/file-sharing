# Generated by Django 4.0.1 on 2022-01-08 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0003_showdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceToDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmpname', models.CharField(blank=True, max_length=50, null=True, verbose_name='company Name')),
                ('invoiceNo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Invoice Number')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Invoice Date')),
                ('gstRegistrationNo', models.CharField(blank=True, max_length=50, null=True, verbose_name='GST Registration No')),
            ],
        ),
        migrations.AlterField(
            model_name='showdata',
            name='email',
            field=models.CharField(default='', max_length=50, verbose_name='Your_Email'),
        ),
        migrations.AlterField(
            model_name='showdata',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Your_Name'),
        ),
    ]
