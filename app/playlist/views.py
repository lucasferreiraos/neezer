from rest_framework import mixins, permissions, viewsets

from .filterset import PlaylistFilterSet
from .models import Playlist
from .serializers import PlaylistSerializer

from django_filters import rest_framework as filters


class PlaylistViewSet(viewsets.ModelViewSet):

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PlaylistFilterSet
