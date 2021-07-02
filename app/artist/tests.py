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

    def test_api_list_artists(self):
        response = self.client.get('/artist/artist/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_api_create_artist(self):
        data = {'name': 'Pepeu Gomes', 'genre': 'MPB'}
        response = self.client.post('/artist/artist/', data)
        self.assertEqual(response.status_code, 201)

    def test_api_update_artist(self):
        data = {'name': 'Edson Gomes', 'genre': 'REG'}
        response = self.client.put(f'/artist/artist/{self.artist_02.id}/', data)
        self.assertEqual(response.status_code, 200)

    def test_api_partial_update_name_artist(self):
        data = {'name': 'Cavaleiros do Forró'}
        response = self.client.patch(f'/artist/artist/{self.artist_02.id}/', data)
        self.assertEqual(response.status_code, 200)

    def test_api_delete_artist(self):
        response = self.client.delete(f'/artist/artist/{self.artist_01.id}/')
        self.assertEqual(response.status_code, 204)
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
            name='Xand Avião', genre='FOR'
        )
        self.artist_03 = Artist.objects.create(
            name='Baco Exu do Blues', genre='RAP'
        )

        self.track_01 = Track.objects.create(
            title='Spread Your Fire', artist=self.artist_01
        )
        self.track_02 = Track.objects.create(
            title='Late Redemption', artist=self.artist_01
        )
        self.track_03 = Track.objects.create(
            title='Inquilina', artist=self.artist_02
        )
        self.track_04 = Track.objects.create(
            title='Baby me Atende', artist=self.artist_02
        )
        self.track_05 = Track.objects.create(
            title='Te Amo Disgraça', artist=self.artist_03
        )
        self.track_06 = Track.objects.create(
            title='Flamingos', artist=self.artist_03
        )

    def test_api_list_tracks(self):
        response = self.client.get('/artist/track/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 6)

    def test_api_create_track(self):
        data = {'title': 'Silence and Distance', 'artist': self.artist_01.id}
        response = self.client.post('/artist/track/', data)
        self.assertEqual(response.status_code, 201)

    def test_api_update_track(self):
        data = {'title': 'Awake from Darkness', 'artist': self.artist_01.id}
        response = self.client.put(f'/artist/track/{self.track_06.id}/', data)
        self.assertEqual(response.status_code, 200)

    def test_api_partial_update_title_track(self):
        data = {'title': 'Tardes que Nunca Acabam'}
        response = self.client.patch(f'/artist/track/{self.track_06.id}/', data)
        self.assertEqual(response.status_code, 200)

    def test_delete_track(self):
        response = self.client.delete(f'/artist/track/{self.track_03.id}/')
        self.assertEqual(response.status_code, 204)
