# Generated by Django 5.0.3 on 2024-04-16 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_instruments', '0002_category_image_country_flag_image_people_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='image',
        ),
    ]
