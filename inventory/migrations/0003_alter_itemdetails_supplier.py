# Generated by Django 4.2.5 on 2024-09-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0002_alter_itemdetails_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemdetails",
            name="supplier",
            field=models.CharField(max_length=30),
        ),
    ]
