from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from artist.models import Track


class Playlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20, verbose_name=_('Nome'))
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name=_('Proprietário(a)')
    )
    tracks = models.ManyToManyField(
        Track, blank=True, verbose_name=_('Músicas')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'
