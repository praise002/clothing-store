# Generated by Django 4.2.6 on 2023-11-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_alter_user_is_superuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
