# Generated by Django 3.2.4 on 2021-06-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210610_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacations',
            name='description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vacations',
            name='from_date_time',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vacations',
            name='to_date_time',
            field=models.CharField(max_length=30),
        ),
    ]
