from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class RegistrationTestCase(APITestCase):

    def test_register(self):
        data={
            'username':'testcase',
            'email':'testcase@abc.com',
            'password':'password',
            'password2':'password'
        }

        response=self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LoginLogoutTestCase(APITestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='username', password='password')

    def test_login(self):
        data={
            'username':'username',
            'password':'password'
        }

        response=self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token,created=Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        response=self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)