from rest_framework import permissions, viewsets

from .filterset import ArtistFilterSet, TrackFilterSet
from .models import Artist, Track
from .serializers import ArtistSerializer, TrackSerializer

from django_filters import rest_framework as filters


class ArtistViewSet(viewsets.ModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ArtistFilterSet


class TrackViewSet(viewsets.ModelViewSet):

    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TrackFilterSet
