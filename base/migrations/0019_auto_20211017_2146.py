# Generated by Django 2.2.24 on 2021-10-17 21:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20211017_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='personal_no',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')]),
        ),
    ]