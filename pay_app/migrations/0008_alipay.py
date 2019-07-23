# Generated by Django 2.0.7 on 2019-07-12 08:33

from django.db import migrations, models
import pay_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_app', '0007_auto_20190712_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='AliPay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('app_id', models.CharField(max_length=20)),
                ('notify_url', models.CharField(blank=True, max_length=100, null=True, verbose_name='回调链接')),
                ('ali_pub_key', models.FileField(blank=True, null=True, upload_to=pay_app.models.key_path, verbose_name='证书key')),
                ('app_pri_key', models.FileField(blank=True, null=True, upload_to=pay_app.models.cert_path, verbose_name='证书')),
                ('app_pub_key', models.FileField(blank=True, null=True, upload_to=pay_app.models.cert_path, verbose_name='证书')),
            ],
            options={
                'verbose_name': '支付宝支付',
                'verbose_name_plural': '支付宝支付',
                'db_table': 'ali_pay',
            },
        ),
    ]