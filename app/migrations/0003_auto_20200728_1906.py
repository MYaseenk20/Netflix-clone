# Generated by Django 3.0.3 on 2020-07-28 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200728_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('ROMANCE', 'ROMANCE'), ('DRAMA', 'DRAMA'), ('ACTION', 'ACTION'), ('COMEDY', 'COMEDY')], max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('EN', 'ENGLISH'), ('GR', 'GERMAN')], max_length=200),
        ),
    ]