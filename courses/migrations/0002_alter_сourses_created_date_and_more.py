# Generated by Django 4.1.1 on 2022-10-08 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="сourses",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 8, 21, 48, 47, 260939)
            ),
        ),
        migrations.AlterField(
            model_name="сourses",
            name="job_openings",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
