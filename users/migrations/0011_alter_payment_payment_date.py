# Generated by Django 5.0.1 on 2024-02-29 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_payment_payment_date_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 29, 10, 24, 57, 236169, tzinfo=datetime.timezone.utc), verbose_name='Дата платежа'),
        ),
    ]
