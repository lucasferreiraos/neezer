from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class ApiAuthTest(TestCase):
    
    def setUp(self):
        url_get_token = reverse('authentication:token_obtain_pair')
        username = 'lucas'
        email = 'lucas@example.com'
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

    def test_register_user(self):
        data = {
            'username': 'joao',
            'email': 'joao@example.com',
            'password': 'senhasegura',
            'confirm_password': 'senhasegura',
            'first_name': 'João',
            'last_name': 'Calazans',
        }
        response = self.client.post('/auth/register/', data)
        self.assertEqual(response.status_code, 201)

    def test_register_user_with_wrong_password(self):
        data = {
            'username': 'joao',
            'email': 'joao@example.com',
            'password': 'senhasegura',
            'confirm_password': 'senhaseguraa',
            'first_name': 'João',
            'last_name': 'Calazans',
        }
        response = self.client.post('/auth/register/', data)
        self.assertEqual(response.status_code, 400)
