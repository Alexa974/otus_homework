# Generated by Django 4.2 on 2023-04-30 19:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0004_alter_card_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="name",
            field=models.CharField(
                blank=True, default="Карточка ", max_length=32, null=True
            ),
        ),
    ]