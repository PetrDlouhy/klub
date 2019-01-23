# Generated by Django 2.1.2 on 2018-12-11 16:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0013_telephone_is_primary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telephone',
            name='is_primary',
            field=models.BooleanField(blank=True, default=False, verbose_name='Primary phone'),
        ),
        migrations.AlterField(
            model_name='telephone',
            name='telephone',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator('^\\+?(42(0|1){1})?\\s?\\d{3}\\s?\\d{3}\\s?\\d{3}$', 'Telephone must consist of numbers, spaces and + sign or maximum number count is higher.')], verbose_name='Telephone'),
        ),
    ]