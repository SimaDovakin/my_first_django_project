# Generated by Django 3.2 on 2021-06-14 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_news_on_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='on_main',
            field=models.BooleanField(default=False, verbose_name='На главную'),
        ),
    ]
