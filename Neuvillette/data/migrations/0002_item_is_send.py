# Generated by Django 4.2.6 on 2023-11-20 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item", name="is_send", field=models.BooleanField(default=False),
        ),
    ]