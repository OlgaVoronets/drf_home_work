# Generated by Django 5.0.1 on 2024-03-01 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_payment_course_alter_payment_lesson_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 1, 9, 12, 13, 146030, tzinfo=datetime.timezone.utc), verbose_name='Дата платежа'),
        ),
    ]
