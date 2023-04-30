# Generated by Django 4.2 on 2023-04-30 14:01

import django.core.validators
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accomplishment",
            name="challenge",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="accomplishment",
            name="notes",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="accomplishment",
            name="reward",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="accomplishment",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
