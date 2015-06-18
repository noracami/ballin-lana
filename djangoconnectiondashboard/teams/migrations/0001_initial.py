# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceItem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('service_item_name', models.CharField(verbose_name='系統名稱', max_length=20)),
                ('service_item_status', models.BooleanField(verbose_name='狀況正常', default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceItemMessage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_fine', models.BooleanField(verbose_name='狀況正常', default=False)),
                ('notes', models.CharField(verbose_name='訊息', max_length=140, default='', blank=True)),
                ('update_time', models.DateTimeField(verbose_name='存取時間', auto_now_add=True)),
                ('comment_user', models.CharField(verbose_name='提供者', max_length=20, default='anonymous')),
                ('service_item', models.ForeignKey(related_name='messages', to='teams.ServiceItem')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('team_name', models.CharField(verbose_name='單位名稱', max_length=20)),
                ('team_order', models.IntegerField(verbose_name='排序')),
            ],
        ),
        migrations.AddField(
            model_name='serviceitem',
            name='team',
            field=models.ForeignKey(related_name='service_items', to='teams.Team'),
        ),
    ]
