# Generated by Django 4.2 on 2023-04-30 19:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0011_rename_name_card_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="card",
            name="title",
        ),
    ]
