# Generated by Django 2.1.1 on 2018-12-25 07:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20181224_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pay_method',
            field=models.CharField(choices=[('btc', 'BTC'), ('eth', 'ETH')], default='btc', max_length=3),
        ),
        migrations.AddField(
            model_name='order',
            name='place',
            field=models.CharField(choices=[('hotel', 'Hotel'), ('sauna', 'Sauna'), ('apprt', 'Appartaments'), ('girl', "Girl's place")], default='hotel', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_choosen',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 25, 7, 3, 12, 591648, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.CharField(choices=[('massage', 'Massage'), ('sex', 'Sex'), ('escort', 'Escort')], max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='value',
            field=models.CharField(choices=[('1', '1 hour'), ('2', '2 hours'), ('night', 'Full Night'), ('day', '1 Day')], max_length=30),
        ),
    ]
