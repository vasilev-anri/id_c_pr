# Generated by Django 2.2.12 on 2021-11-09 17:29

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_auto_20211109_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='description',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Shift', ((1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fixed'), (5, 'Rotating'), (6, 'Split'), (7, 'On-call'))), ('Job level', ((1, 'Intern'), (2, 'Junior'), (3, 'Middle'), (4, 'Senior'), (5, 'Lead'))), ('Employment form', ((1, 'Full-time'), (2, 'Part-time'))), ('Experience', ((1, 'Without experience'), (2, 'Less than 1 year'), (3, '1 - 2 years'), (4, '2 - 3 years'), (5, '3 - 5 years'), (6, '5 - 7 years'), (7, '7 - 10 years'), (8, '10+ years')))], default='description', max_length=80),
        ),
    ]