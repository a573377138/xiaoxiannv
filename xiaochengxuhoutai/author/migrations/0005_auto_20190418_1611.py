# Generated by Django 2.0.2 on 2019-04-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_auto_20190418_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='头像'),
        ),
    ]
