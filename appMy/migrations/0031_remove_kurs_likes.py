# Generated by Django 4.2.7 on 2024-01-17 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0030_kurs_likes_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kurs',
            name='likes',
        ),
    ]
