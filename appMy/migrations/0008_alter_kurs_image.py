# Generated by Django 4.2.7 on 2024-01-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0007_alter_kurs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurs',
            name='image',
            field=models.ImageField(upload_to=None, verbose_name='Resim'),
        ),
    ]