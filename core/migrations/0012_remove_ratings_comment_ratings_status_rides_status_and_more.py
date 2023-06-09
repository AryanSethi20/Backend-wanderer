# Generated by Django 4.1.7 on 2023-04-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_rides_end_lat_rides_start_lat_userprofiles_address_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ratings",
            name="comment",
        ),
        migrations.AddField(
            model_name="ratings",
            name="status",
            field=models.CharField(
                choices=[("Pending", "Pending"), ("Completed", "Completed")],
                default="Pending",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="rides",
            name="status",
            field=models.CharField(
                choices=[
                    ("Open", "Open"),
                    ("Closed", "Closed"),
                    ("Completed", "Completed"),
                ],
                default="Open",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="ratings",
            name="rating",
            field=models.IntegerField(
                choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")], default=1
            ),
        ),
    ]
