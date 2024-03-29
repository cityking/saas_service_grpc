# Generated by Django 2.0.7 on 2019-06-19 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeixinPay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('app_id', models.CharField(max_length=20)),
                ('mch_id', models.CharField(max_length=20)),
                ('mch_key', models.CharField(max_length=20)),
                ('notify_url', models.CharField(max_length=20, null=True, verbose_name='回调链接')),
                ('cert_key', models.CharField(max_length=20, null=True, verbose_name='证书key')),
                ('cert', models.CharField(max_length=20, null=True, verbose_name='证书')),
            ],
            options={
                'verbose_name': '微信支付',
                'verbose_name_plural': '微信支付',
                'db_table': 'weixin_pay',
            },
        ),
    ]
