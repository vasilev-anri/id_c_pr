# Generated by Django 2.2.12 on 2021-11-24 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0106_info_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='name',
        ),
    ]