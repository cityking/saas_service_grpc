# Generated by Django 2.0.7 on 2019-06-19 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_app', '0002_auto_20190619_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weixinpay',
            name='notify_url',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='回调链接'),
        ),
    ]
