from .models import Artist, Track

from utils.filterset import SearchFilterSet

from django_filters.filters import ChoiceFilter


FILTER_GENRE_CHOICES = [
    ('axe', 'Axé'), ('pagode', 'Pagode'),
    ('samba', 'Samba'), ('sertanejo', 'Sertanejo'),
    ('forro', 'Forró'), ('pop', 'Pop'),
    ('rock', 'Rock'), ('metal', 'Metal'),
    ('funk', 'Funk'), ('reggae', 'Reggae'),
    ('erudito', 'Erudito'), ('rap', 'Rap'),
    ('mpb', 'Mpb'), ('arrocha', 'Arrocha'),
    ('instrumental', 'Instrumental')
]

class ArtistFilterSet(SearchFilterSet):
    filter_by = ChoiceFilter(
        choices=FILTER_GENRE_CHOICES,
        method='filter_by_genre'
    )

    class Meta:
        model = Artist
        fields = ['q', 'filter_by']
        search_fields = [
            'name__icontains',
        ]

    def filter_by_genre(self, queryset, name, value):
        if value == 'axe':
            return queryset.filter(genre='AXE')
        elif value == 'pagode':
            return queryset.filter(genre='PAG')
        elif value == 'samba':
            return queryset.filter(genre='SAM')
        elif value == 'sertanejo':
            return queryset.filter(genre='SER')
        elif value == 'forro':
            return queryset.filter(genre='FOR')
        elif value == 'pop':
            return queryset.filter(genre='POP')
        elif value == 'rock':
            return queryset.filter(genre='ROC')
        elif value == 'metal':
            return queryset.filter(genre='MET')
        elif value == 'funk':
            return queryset.filter(genre='FUN')
        elif value == 'reggae':
            return queryset.filter(genre='REG')
        elif value == 'erudito':
            return queryset.filter(genre='ERU')
        elif value == 'rap':
            return queryset.filter(genre='RAP')
        elif value == 'mpb':
            return queryset.filter(genre='MPB')
        elif value == 'arrocha':
            return queryset.filter(genre='ARR')
        elif value == 'instrumental':
            return queryset.filter(genre='INS')
        return queryset


class TrackFilterSet(SearchFilterSet):

    class Meta:
        model = Track
        fields = ['q']
        search_fields = [
            'title__icontains',
            'artist__name__icontains',
            'album__icontains',
            'release_year__icontains',
        ]
