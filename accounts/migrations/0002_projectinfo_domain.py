# Generated by Django 3.2.4 on 2021-06-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='domain',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]