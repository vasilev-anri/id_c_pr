# Generated by Django 2.2.12 on 2021-11-21 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0083_delete_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Department'),
        ),
    ]
