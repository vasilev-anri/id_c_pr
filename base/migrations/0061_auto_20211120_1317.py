# Generated by Django 2.2.12 on 2021-11-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0060_department_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department',
            field=models.CharField(default='', max_length=100),
        ),
    ]