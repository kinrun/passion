# Generated by Django 2.1.4 on 2018-12-23 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181223_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='value',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
