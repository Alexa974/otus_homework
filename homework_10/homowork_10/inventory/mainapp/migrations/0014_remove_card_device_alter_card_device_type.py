# Generated by Django 4.2 on 2023-04-30 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0013_card_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="card",
            name="device",
        ),
        migrations.AlterField(
            model_name="card",
            name="device_type",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="mainapp.device",
            ),
            preserve_default=False,
        ),
    ]