# Generated by Django 2.0.7 on 2019-08-09 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_app', '0010_auto_20190716_0739'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayPalPay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('client_id', models.CharField(max_length=200)),
                ('client_secret', models.CharField(max_length=200)),
                ('return_url', models.CharField(blank=True, max_length=500, null=True)),
                ('cancel_url', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]