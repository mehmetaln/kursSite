# Generated by Django 4.2.7 on 2024-01-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0030_alter_kurs_date_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurs',
            name='date_now',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Tarih - Saat'),
        ),
    ]