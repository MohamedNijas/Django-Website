# Generated by Django 4.1.7 on 2023-03-04 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="listings",
            name="image",
            field=models.ImageField(default="", upload_to=""),
            preserve_default=False,
        ),
    ]
