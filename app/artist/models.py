from uuid import uuid4

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Artist(models.Model):
    GENRE_CHOICES = [
        ('AXE', 'Axé'), ('PAG', 'Pagode'),
        ('SAM', 'Samba'), ('SER', 'Sertanejo'),
        ('FOR', 'Forró'), ('POP', 'Pop'),
        ('ROC', 'Rock'), ('MET', 'Metal'),
        ('FUN', 'Funk'), ('REG', 'Reggae'),
        ('ERU', 'Erudito'), ('RAP', 'Rap'),
        ('MPB', 'Mpb'), ('ARR', 'Arrocha'),
        ('INS', 'Instrumental')
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20, verbose_name=_('Nome'))
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES, verbose_name=_('Gênero'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Artista')
        verbose_name_plural = _('Artistas')


class Track(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=30, verbose_name=_('Título'))
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, verbose_name=_('Artista')
    )
    album = models.CharField(
        max_length=30, verbose_name=_('Álbum'),
        null=True, blank=True
    )
    release_year = models.CharField(
        max_length=30, verbose_name=_('Ano de lançamento'),
        null=True, blank=True
    )

    def __str__(self):
        return f'{self.title} - {self.artist}'

    class Meta:
        verbose_name = _('Música')
        verbose_name_plural = _('Músicas')
