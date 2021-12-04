# Generated by Django 3.2.3 on 2021-05-30 19:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0013_auto_20210530_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2021, 5, 30, 21, 50, 8, 984446))),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.users')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.products')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
