# Generated by Django 2.2.1 on 2019-06-16 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0010_auto_20190413_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='privacy',
            field=models.BooleanField(default=True),
        ),
    ]
