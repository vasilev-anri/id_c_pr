# Generated by Django 2.2.12 on 2021-11-20 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0053_auto_20211120_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='students',
        ),
        migrations.AddField(
            model_name='department',
            name='students',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='base.Info'),
        ),
    ]
