# Generated by Django 4.2.2 on 2023-12-15 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]