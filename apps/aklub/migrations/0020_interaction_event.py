# Generated by Django 2.1.5 on 2019-01-20 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0019_auto_20190120_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaction',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='aklub.Event'),
        ),
    ]
