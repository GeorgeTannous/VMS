# Generated by Django 3.2.4 on 2021-06-08 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_vacations_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacations',
            name='request_status',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vacations',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]