from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Artist, Track


class ApiArtistTest(TestCase):

    def setUp(self):
        url_get_token = reverse('authentication:token_obtain_pair')
        username = 'admin'
        email = 'admin@example.com'
        password = '12345678'

        self.user = User.objects.create(
            username=username, email=email
        )
        self.user.set_password(password)
        self.user.save()

        self.client = APIClient()
        resp = self.client.post(
            url_get_token,
            {'username': username, 'password': password},
            format='json'
        )
        token = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        self.artist_01 = Artist.objects.create(
            name='Angra', genre='MET'
        )
        self.artist_02 = Artist.objects.create(
            name='Xand Avião', genre='FOR'
        )
        self.artist_03 = Artist.objects.create(
            name='Baco Exu do Blues', genre='RAP'
        )
        self.artist_04 = Artist.objects.create(
            name='Sepultura', genre='MET'
        )
        self.artist_05 = Artist.objects.create(
            name='Magníficos', genre='FOR'
        )
        self.artist_06 = Artist.objects.create(
            name='Dorgival Dantas', genre='FOR'
        )
        self.artist_07 = Artist.objects.create(
            name='Gusttavo Lima', genre='SER'
        )
        self.artist_08 = Artist.objects.create(
            name='Lauana Prado', genre='SER'
        )
        self.artist_09 = Artist.objects.create(
            name='Maneva', genre='REG'
        )

    def test_api_list_artists(self):
        response = self.client.get('/artist/artist/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 9)

    def test_api_create_artist(self):
        data = {'name': 'Pepeu Gomes', 'genre': 'MPB'}
        response = self.client.post('/artist/artist/', data)
        self.assertEqual(response.status_code, 201)

    def test_api_update_artist(self):
        data = {'name': 'Edson Gomes', 'genre': 'REG'}
        response = self.client.put(
            f'/artist/artist/{self.artist_02.id}/', data
        )
        self.assertEqual(response.status_code, 200)

    def test_api_partial_update_name_artist(self):
        data = {'name': 'Cavaleiros do Forró'}
        response = self.client.patch(
            f'/artist/artist/{self.artist_02.id}/', data
        )
        self.assertEqual(response.status_code, 200)

    def test_api_delete_artist(self):
        response = self.client.delete(f'/artist/artist/{self.artist_01.id}/')
        self.assertEqual(response.status_code, 204)

    def test_api_search_artist_by_id(self):
        response = self.client.get(f'/artist/artist/{self.artist_08.id}/')
        self.assertEqual(response.status_code, 200)

    def test_api_search_artist_by_name(self):
        response = self.client.get('/artist/artist/?q=dor')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_api_search_artist_by_metal_genre(self):
        response = self.client.get('/artist/artist/?filter_by=metal')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_api_search_artist_by_forro_genre(self):
        response = self.client.get('/artist/artist/?filter_by=forro')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)


class ApiTrackTest(TestCase):

    def setUp(self):
        url_get_token = reverse('authentication:token_obtain_pair')
        username = 'admin'
        email = 'admin@example.com'
        password = '12345678'

        self.user = User.objects.create(
            username=username, email=email
        )
        self.user.set_password(password)
        self.user.save()

        self.client = APIClient()
        resp = self.client.post(
            url_get_token,
            {'username': username, 'password': password},
            format='json'
        )
        token = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        self.artist_01 = Artist.objects.create(
            name='Angra', genre='MET'
        )
        self.artist_02 = Artist.objects.create(
            name='Gusttavo Lima', genre='SER'
        )
        self.artist_03 = Artist.objects.create(
            name='Baco Exu do Blues', genre='RAP'
        )
        self.artist_04 = Artist.objects.create(
            name='Djonga', genre='RAP'
        )

        self.track_01 = Track.objects.create(
            title='Spread Your Fire', artist=self.artist_01,
            album='Temple of Shadows', release_year='2004'
        )
        self.track_02 = Track.objects.create(
            title='Late Redemption', artist=self.artist_01,
            album='Temple of Shadows', release_year='2004'
        )
        self.track_03 = Track.objects.create(
            title='Unholy Wars', artist=self.artist_01,
            album='Rebirth', release_year='2001'
        )
        self.track_04 = Track.objects.create(
            title='Contador de Reencontros', artist=self.artist_02,
            album='O Embaixador in Cariri', release_year='2019'
        )
        self.track_05 = Track.objects.create(
            title='Perrengue', artist=self.artist_02,
            album='O Embaixador in Cariri', release_year='2019'
        )
        self.track_06 = Track.objects.create(
            title='Flamingos', artist=self.artist_03,
            album='Bluesman', release_year='2018'
        )
        self.track_07 = Track.objects.create(
            title='Me Desculpa Jay Z', artist=self.artist_03,
            album='Bluesman', release_year='2018'
        )
        self.track_08 = Track.objects.create(
            title='1010', artist=self.artist_04,
            album='O Menino Que Queria Ser Deus', release_year='2018'
        )
        self.track_09 = Track.objects.create(
            title='Leal', artist=self.artist_04,
            album='Ladrão', release_year='2019'
        )
        self.track_10 = Track.objects.create(
            title='Hat Trick', artist=self.artist_04,
            album='Ladrão', release_year='2019'
        )

    def test_api_list_tracks(self):
        response = self.client.get('/artist/track/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 10)

    def test_api_create_track(self):
        data = {'title': 'Silence and Distance', 'artist': self.artist_01.id}
        response = self.client.post('/artist/track/', data)
        self.assertEqual(response.status_code, 201)

    def test_api_update_track(self):
        data = {'title': 'Awake from Darkness', 'artist': self.artist_01.id}
        response = self.client.put(
            f'/artist/track/{self.track_06.id}/', data
        )
        self.assertEqual(response.status_code, 200)

    def test_api_partial_update_title_track(self):
        data = {'title': 'Tardes que Nunca Acabam'}
        response = self.client.patch(
            f'/artist/track/{self.track_06.id}/', data
        )
        self.assertEqual(response.status_code, 200)

    def test_api_delete_track(self):
        response = self.client.delete(f'/artist/track/{self.track_03.id}/')
        self.assertEqual(response.status_code, 204)

    def test_api_search_track_by_artist_from_incomplete_term(self):
        response = self.client.get('/artist/track/?q=an')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)

    def test_api_search_track_by_artist_from_full_artist_name(self):
        response = self.client.get('/artist/track/?q=djonga')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_api_search_track_by_artist_from_release_year(self):
        response = self.client.get('/artist/track/?q=2019')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

    def test_api_search_track_by_artist_from_full_album_name(self):
        response = self.client.get('/artist/track/?q=rebirth')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
