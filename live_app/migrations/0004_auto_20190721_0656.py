# Generated by Django 2.0.7 on 2019-07-21 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_app', '0003_auto_20190721_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveplayback',
            name='live_info',
            field=models.CharField(max_length=100, null=True, verbose_name='直播信息'),
        ),
        migrations.AddField(
            model_name='liveplayback',
            name='media_type',
            field=models.IntegerField(default=0, verbose_name='视频类型'),
        ),
    ]
