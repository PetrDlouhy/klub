# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0039_auto_20161221_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxconfirmation',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aklub.UserProfile'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='result',
            field=models.ManyToManyField(blank=True, to='aklub.Result', verbose_name='Acceptable results of communication'),
        ),
        migrations.AlterField(
            model_name='masscommunication',
            name='template',
            field=models.TextField(help_text='Template can contain variable substitutions like addressment, name, variable symbol etc.', max_length=50000, null=True, verbose_name='Template'),
        ),
    ]