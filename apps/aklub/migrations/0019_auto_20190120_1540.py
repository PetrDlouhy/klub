# Generated by Django 2.1.5 on 2019-01-20 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0018_auto_20190120_1534'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Campaign',
            new_name='Event',
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
    ]
