# Generated by Django 4.2.7 on 2024-01-03 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0016_facetofacecategory_onlinecategory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kurs',
            old_name='category',
            new_name='facetofacecategory',
        ),
        migrations.AddField(
            model_name='kurs',
            name='onlinecategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.onlinecategory', verbose_name='Kategori'),
        ),
    ]