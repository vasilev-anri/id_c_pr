# Generated by Django 2.2.12 on 2021-11-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='description',
        ),
        migrations.AlterField(
            model_name='description',
            name='d',
            field=models.ManyToManyField(choices=[('Shift', (('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fixed', 'Fixed'), ('Rotating', 'Rotating'), ('Split', 'Split'), ('On-call', 'On-call'))), ('Employment form', (('Full-time', 'Full-time'), ('Part-time', 'Part-time'))), ('Experience', (('Without experience', 'Without experience'), ('Less than 1 year', 'Less than 1 year'), ('1 - 2 years', '1 - 2 years'), ('2 - 3 years', '2 - 3 years'), ('3 - 5 years', '3 - 5 years'), ('5 - 7 years', '5 - 7 years'), ('7 - 10 years', '7 - 10 years'), ('10+ years', '10+ years'))), ('English language level', (('Intermediate/B1', 'Intermediate/B1'), ('Upper Intermediate/B2', 'Upper Intermediate/B2'), ('Pre-advanced/C1', 'Pre-advanced/C1'), ('Advanced/C2', 'Advanced/C2')))], to='base.Info'),
        ),
    ]
