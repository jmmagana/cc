# Generated by Django 3.0.2 on 2020-04-16 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0048_auto_20200416_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_status',
            field=models.CharField(default='Defaul value', max_length=15),
        ),
    ]