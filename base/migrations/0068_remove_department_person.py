# Generated by Django 2.2.12 on 2021-11-20 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0067_department_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='person',
        ),
    ]
