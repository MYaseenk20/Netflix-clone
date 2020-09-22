# Generated by Django 3.0.3 on 2020-08-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200807_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('Comedy', 'Comedy'), ('romance', 'Romance'), ('Action', 'Action'), ('Drama', 'Drama')], max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('English', 'ENGLISH'), ('German', 'GERMAN')], max_length=200),
        ),
    ]