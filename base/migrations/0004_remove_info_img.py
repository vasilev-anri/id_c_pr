# Generated by Django 2.2.12 on 2021-10-13 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_info_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='img',
        ),
    ]