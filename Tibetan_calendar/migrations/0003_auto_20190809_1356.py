# Generated by Django 2.0.7 on 2019-08-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tibetan_calendar', '0002_auto_20190724_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='tibetancalendar',
            name='shareUrl',
            field=models.CharField(max_length=200, null=True, verbose_name='分享链接'),
        ),
        migrations.AddField(
            model_name='tibetancalendar',
            name='tibetanDay',
            field=models.CharField(max_length=200, null=True, verbose_name='藏历日'),
        ),
        migrations.AddField(
            model_name='tibetancalendar',
            name='tibetanMonth',
            field=models.CharField(max_length=200, null=True, verbose_name='藏历月'),
        ),
        migrations.AddField(
            model_name='tibetancalendar',
            name='tibetanYear',
            field=models.CharField(max_length=200, null=True, verbose_name='藏历年'),
        ),
    ]
