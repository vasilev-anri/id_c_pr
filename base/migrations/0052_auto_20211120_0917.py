# Generated by Django 2.2.12 on 2021-11-20 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0051_remove_tag_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='person',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='base.Info'),
        ),
    ]