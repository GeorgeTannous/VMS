# Generated by Django 3.2.4 on 2021-06-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210608_1219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacations',
            options={},
        ),
        migrations.AlterField(
            model_name='vacations',
            name='to_date_time',
            field=models.DateTimeField(verbose_name='%m/%d/%Y %H:%M'),
        ),
    ]