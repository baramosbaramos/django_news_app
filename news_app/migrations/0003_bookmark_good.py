# Generated by Django 3.1.7 on 2021-03-23 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_auto_20210322_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='good',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
