# Generated by Django 4.2.6 on 2023-11-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0006_line_lineaddress"),
    ]

    operations = [
        migrations.RemoveField(model_name="item", name="client_id",),
        migrations.AddField(
            model_name="item",
            name="addressee_id",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="item",
            name="addressee_telephone_number",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="item",
            name="receive_address",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="item",
            name="sender_id",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="item",
            name="sender_telephone_number",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="item",
            name="ship_address",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="item",
            name="item_id",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="item",
            name="receive_address_id",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="item",
            name="ship_address_id",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="item",
            name="weight",
            field=models.CharField(default="", max_length=100),
        ),
    ]
