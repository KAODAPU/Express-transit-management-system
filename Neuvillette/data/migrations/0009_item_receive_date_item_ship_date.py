# Generated by Django 4.2.6 on 2023-12-03 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0008_remove_item_receive_date_remove_item_ship_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="receive_date",
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name="item",
            name="ship_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 3, 17, 2, 58, 255943)
            ),
        ),
    ]
