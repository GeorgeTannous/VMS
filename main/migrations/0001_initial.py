# Generated by Django 3.2.4 on 2021-06-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
            ],
        ),
    ]
