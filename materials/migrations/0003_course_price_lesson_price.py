# Generated by Django 5.0.1 on 2024-02-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_course_owner_lesson_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.PositiveIntegerField(default=1000, verbose_name='Цена, руб.'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='price',
            field=models.PositiveIntegerField(default=1000, verbose_name='Цена, руб.'),
        ),
    ]
