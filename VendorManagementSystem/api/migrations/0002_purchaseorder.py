# Generated by Django 5.0.4 on 2024-04-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PurchaseOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("po_number", models.UUIDField(verbose_name="A5D5C83A")),
                ("vendor_reference", models.CharField(max_length=100)),
                ("order_date", models.DateField()),
                ("items", models.TextField()),
                ("quantity", models.IntegerField()),
                ("status", models.BooleanField(default=False)),
            ],
        ),
    ]