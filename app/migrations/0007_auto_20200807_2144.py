# Generated by Django 3.0.3 on 2020-08-07 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200802_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('romance', 'Romance')], max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('MW', 'MOST WATCHED'), ('TR', 'TOP RATED'), ('RA', 'RECENTLY ADDED')], max_length=200),
        ),
    ]
