# Generated by Django 2.2.12 on 2021-11-21 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0086_auto_20211121_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='department',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Department'),
        ),
    ]
