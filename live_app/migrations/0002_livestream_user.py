# Generated by Django 2.0.7 on 2019-07-19 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestream',
            name='user',
            field=models.ForeignKey(default=1, on_delete=None, to='live_app.LiveUser', verbose_name='用户'),
            preserve_default=False,
        ),
    ]