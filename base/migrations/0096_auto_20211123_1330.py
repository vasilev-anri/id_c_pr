# Generated by Django 2.2.12 on 2021-11-23 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0095_auto_20211123_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Department'),
        ),
    ]
