# Generated by Django 3.1.7 on 2021-03-22 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='question',
            new_name='user',
        ),
    ]