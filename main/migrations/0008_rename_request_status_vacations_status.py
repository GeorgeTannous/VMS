# Generated by Django 3.2.4 on 2021-06-08 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210608_1008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacations',
            old_name='request_status',
            new_name='status',
        ),
    ]
