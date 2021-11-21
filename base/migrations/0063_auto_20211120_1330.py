# Generated by Django 2.2.12 on 2021-11-20 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0062_auto_20211120_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Department'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.Info'),
        ),
    ]
