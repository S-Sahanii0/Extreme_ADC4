# Generated by Django 2.2.7 on 2020-01-16 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endUser', '0002_auto_20200116_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='userName',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='userName',
            new_name='username',
        ),
    ]
