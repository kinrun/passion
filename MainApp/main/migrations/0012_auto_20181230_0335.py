# Generated by Django 2.1.4 on 2018-12-30 00:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20181225_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='active_flag',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Requested by Buyer'), ('b', 'Requested by Seller'), ('1', 'Agreement'), ('2', 'Date and Place choosed'), ('3', 'Seller meet Buyer in life'), ('4', 'Buyer agree to start'), ('5', 'Prolongue'), ('6', 'Order done'), ('7', 'Disput')], default='a', help_text='Current status of Order', max_length=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer', to=settings.AUTH_USER_MODEL, verbose_name='Buyer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_choosen',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 30, 0, 35, 20, 975844, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='place',
            field=models.CharField(choices=[('h', 'Hotel'), ('s', 'Sauna'), ('a', 'Appartaments'), ('g', "Girl's place")], default='h', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller', to=settings.AUTH_USER_MODEL, verbose_name='Seller'),
        ),
        migrations.AlterField(
            model_name='order',
            name='value',
            field=models.CharField(choices=[('1', '1 hour'), ('2', '2 hours'), ('8', 'Night (8 hours)'), ('f', '1 Day (24 hours)')], default='2', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='balance_btc',
            field=models.CharField(blank=True, default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='balance_eth',
            field=models.CharField(blank=True, default='0', max_length=30),
        ),
    ]
