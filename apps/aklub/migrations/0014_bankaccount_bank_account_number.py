# Generated by Django 2.1.5 on 2019-02-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0013_auto_20190201_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='bank_account_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
