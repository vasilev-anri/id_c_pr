# Generated by Django 2.2.12 on 2021-11-20 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0074_auto_20211120_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Department'),
        ),
    ]
