# Generated by Django 3.2.18 on 2023-05-01 13:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230501_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='public_id',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 1, 13, 30, 56, 200939, tzinfo=utc), verbose_name='date of publish'),
        ),
    ]
