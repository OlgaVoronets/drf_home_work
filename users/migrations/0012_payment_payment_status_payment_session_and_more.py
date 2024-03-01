# Generated by Django 5.0.1 on 2024-03-01 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_payment_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_status',
            field=models.BooleanField(default=False, verbose_name='Статус оплаты'),
        ),
        migrations.AddField(
            model_name='payment',
            name='session',
            field=models.TextField(blank=True, null=True, verbose_name='Платежная сессия'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 1, 6, 42, 17, 322122, tzinfo=datetime.timezone.utc), verbose_name='Дата платежа'),
        ),
    ]
