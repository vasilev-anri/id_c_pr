# Generated by Django 2.2.12 on 2021-11-20 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0069_info_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='department',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='person',
        ),
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Department'),
        ),
    ]