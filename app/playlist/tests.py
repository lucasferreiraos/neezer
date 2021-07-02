from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from artist.models import Artist, Track
from .models import Playlist


class ApiPlayListTest(TestCase):

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
            name='Guthrie Govan', genre='INS'
        )
        self.artist_02 = Artist.objects.create(
            name='Kiko Loureiro', genre='INS'
        )
        self.artist_03 = Artist.objects.create(
            name='Polyphia', genre='INS'
        )

        self.track_01 = Track.objects.create(
            title='Mãe d`Água', artist=self.artist_02
        )
        self.track_02 = Track.objects.create(
            title='Edm (E-Dependent Mind)', artist=self.artist_02
        )
        self.track_03 = Track.objects.create(
            title='Erotic Cakes', artist=self.artist_01
        )
        self.track_04 = Track.objects.create(
            title='Waves', artist=self.artist_01
        )
        self.track_05 = Track.objects.create(
            title='G.O.A.T.', artist=self.artist_03
        )
        self.track_06 = Track.objects.create(
            title='Goose', artist=self.artist_03
        )

        self.playlist_01 = Playlist.objects.create(
            name='Playlist 01', owner=self.user,
        )
        self.playlist_01.tracks.set([self.track_03, self.track_01])
        self.playlist_02 = Playlist.objects.create(
            name='Playlist 02', owner=self.user,
        )
        self.playlist_02.tracks.set([self.track_04, self.track_06])

    def test_api_list_playlists(self):
        response = self.client.get('/playlist/playlist/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_api_create_playlist_without_songs(self):
        data = {
            'name': 'guitarradas',
            'owner': self.user.id,
            'tracks': []
        }
        response = self.client.post('/playlist/playlist/', data)
        self.assertEqual(response.status_code, 201)

    def test_api_create_playlist_with_songs(self):
        songs = [self.track_02.id, self.track_04.id, self.track_06.id]
        data = {
            'name': 'setlist instrumental',
            'owner': self.user.id,
            'tracks': songs
        }
        response = self.client.post('/playlist/playlist/', data)
        self.assertEqual(response.status_code, 201)

    def test_api_add_song_to_playlist(self):
        songs = [self.track_04.id, self.track_06.id, self.track_01.id]
        data = {'tracks': songs}
        response = self.client.patch(f'/playlist/playlist/{self.playlist_02.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['tracks']), 3)

    def test_api_remove_song_to_playlist(self):
        songs = [self.track_01.id]
        data = {'tracks': songs}
        response = self.client.patch(f'/playlist/playlist/{self.playlist_01.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['tracks']), 1)

    def test_api_delete_playlist(self):
        response = self.client.delete(f'/playlist/playlist/{self.playlist_01.id}/')
        self.assertEqual(response.status_code, 204)
