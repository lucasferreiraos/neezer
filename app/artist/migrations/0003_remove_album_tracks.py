# Generated by Django 3.1.4 on 2021-06-30 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_album_tracks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='tracks',
        ),
    ]
