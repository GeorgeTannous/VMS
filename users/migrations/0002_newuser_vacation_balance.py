# Generated by Django 3.2.4 on 2021-06-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='vacation_balance',
            field=models.DecimalField(decimal_places=1, default=5, max_digits=5),
        ),
    ]
