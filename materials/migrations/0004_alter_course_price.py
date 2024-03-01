# Generated by Django 5.0.1 on 2024-03-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_course_price_lesson_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.PositiveIntegerField(default=100000, verbose_name='Цена, руб.'),
        ),
    ]
