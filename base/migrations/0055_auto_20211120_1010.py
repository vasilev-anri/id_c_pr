# Generated by Django 2.2.12 on 2021-11-20 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0054_auto_20211120_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='students',
        ),
        migrations.AddField(
            model_name='department',
            name='students',
            field=models.ManyToManyField(through='base.Enrollment', to='base.Info'),
        ),
    ]
