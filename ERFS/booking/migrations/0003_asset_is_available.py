# Generated by Django 3.0.1 on 2020-02-02 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20200131_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
