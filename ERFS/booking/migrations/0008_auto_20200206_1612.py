# Generated by Django 3.0.1 on 2020-02-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_remove_asset_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='is_available',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
