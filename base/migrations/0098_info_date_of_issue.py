# Generated by Django 2.2.12 on 2021-11-23 14:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0097_remove_info_date_of_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='date_of_issue',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]