# Generated by Django 3.0.2 on 2020-04-15 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0042_auction_auction_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='auction_status',
        ),
    ]
