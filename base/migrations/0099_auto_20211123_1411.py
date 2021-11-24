# Generated by Django 2.2.12 on 2021-11-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0098_info_date_of_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='name',
            field=models.CharField(blank=True, default='', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='description',
            field=models.ManyToManyField(blank=True, null=True, to='base.Description'),
        ),
    ]
