# Generated by Django 2.2.12 on 2021-11-21 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0085_auto_20211121_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='info',
        ),
        migrations.AddField(
            model_name='department',
            name='department',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='department',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Department'),
        ),
    ]
