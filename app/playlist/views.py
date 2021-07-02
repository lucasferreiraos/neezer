from rest_framework import mixins, permissions, viewsets

from .models import Playlist
from .serializers import PlaylistSerializer


class PlaylistViewSet(viewsets.ModelViewSet):

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]
