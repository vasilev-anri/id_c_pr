# Generated by Django 2.2.12 on 2021-10-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20211015_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='citizenship',
            field=models.CharField(default='GEO', editable=False, max_length=3),
        ),
    ]