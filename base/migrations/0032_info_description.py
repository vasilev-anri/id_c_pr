# Generated by Django 2.2.12 on 2021-11-09 16:35

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_remove_info_d'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='description',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('sample', 'sample'), ('sample', 'sample'), ('sample', 'sample'), ('sample', 'sample')], default='description', max_length=80),
        ),
    ]