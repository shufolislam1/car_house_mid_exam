# Generated by Django 4.2.7 on 2024-02-15 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]