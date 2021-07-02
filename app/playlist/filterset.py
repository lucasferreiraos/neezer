from .models import Playlist

from utils.filterset import SearchFilterSet


class PlaylistFilterSet(SearchFilterSet):

    class Meta:
        model = Playlist
        fields = ['q']
        search_fields = [
            'name__icontains'
        ]
