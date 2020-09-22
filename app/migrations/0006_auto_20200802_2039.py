# Generated by Django 3.0.3 on 2020-08-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200730_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('romance', 'romance'), ('comedy', 'comedy'), ('action', 'action'), ('drama', 'drama')], max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('MW', 'MOST WATCHED'), ('RA', 'RECENTLY ADDED'), ('TR', 'TOP RATED')], max_length=200),
        ),
        migrations.AlterField(
            model_name='movielinks',
            name='type',
            field=models.CharField(choices=[('W', 'WATCH LINK'), ('D', 'DOWNLOAD LINK')], max_length=100),
        ),
    ]
