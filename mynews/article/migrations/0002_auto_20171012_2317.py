# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('pic', models.ImageField(upload_to=b'uploads', verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x9b\xbe')),
                ('adurl', models.URLField(verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80')),
                ('adlocation', models.CharField(max_length=2, verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae')),
                ('status', models.CharField(default=1, max_length=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 12, 23, 17, 35, 642000), verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
    ]
