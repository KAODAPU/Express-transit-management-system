# Generated by Django 4.2.6 on 2023-12-02 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0007_remove_item_client_id_item_addressee_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="item", name="receive_date",),
        migrations.RemoveField(model_name="item", name="ship_date",),
    ]
