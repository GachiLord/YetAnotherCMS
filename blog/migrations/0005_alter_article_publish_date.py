# Generated by Django 3.2.18 on 2023-05-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20230501_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateField(verbose_name='date of publish'),
        ),
    ]
