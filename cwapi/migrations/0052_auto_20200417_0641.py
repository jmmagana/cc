# Generated by Django 3.0.2 on 2020-04-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0051_auto_20200417_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_winner',
            field=models.CharField(editable=False, max_length=25, null=True),
        ),
    ]
