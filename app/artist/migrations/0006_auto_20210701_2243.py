# Generated by Django 3.1.4 on 2021-07-02 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0005_auto_20210701_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Álbum'),
        ),
        migrations.AddField(
            model_name='track',
            name='release_year',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Ano de lançamento'),
        ),
    ]
