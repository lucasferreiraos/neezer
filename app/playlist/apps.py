from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PlaylistConfig(AppConfig):
    name = 'playlist'
    verbose_name = _('Playlist')
