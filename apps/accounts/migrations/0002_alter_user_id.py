# Generated by Django 4.2.6 on 2023-11-02 20:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("bea151d4-d6c1-4155-8b2c-86506f92838b"),
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
