# Generated by Django 4.2.7 on 2024-01-17 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0042_alter_comment_date_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_now',
            field=models.DateTimeField(verbose_name='Tarih ve Saat'),
        ),
    ]
