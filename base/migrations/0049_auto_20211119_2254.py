# Generated by Django 2.2.12 on 2021-11-19 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0048_auto_20211119_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='department',
        ),
        migrations.AddField(
            model_name='department',
            name='department',
            field=models.CharField(default='dep choice', max_length=60),
        ),
    ]