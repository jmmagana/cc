# Generated by Django 3.0.2 on 2020-04-15 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0034_auto_20200414_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_title',
        ),
        migrations.AddField(
            model_name='item',
            name='item',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cwapi.Auction'),
            preserve_default=False,
        ),
    ]
