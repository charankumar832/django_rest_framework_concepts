from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.urls import reverse

from movie_app import models
from movie_app.api import serializers

class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='username', password='password')
        self.token,created=Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

        self.stream=models.StreamPlatform.objects.create(name='netflix', about='netflix vedios', website='netflix.com')

    def test_StreamPlatform_create(self):

        data={
            'name':'prime',
            'about':'prime vedios',
            'website':'primevedios.com'
        }

        response=self.client.post(reverse('stream-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_StreamPlatform_list(self):
        response=self.client.get(reverse('stream-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
    def test_StreamPlatform_indiviual(self):
        response=self.client.get(reverse('stream-detail',args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
    def test_StreamPlatform_update(self):
        data={
            'name':'netflix-updated',
            'about':'netflix vedios-updated',
            'website':'netflix-updated.com'
        }

        response=self.client.put(reverse('stream-detail',args=(self.stream.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_StreamPlatform_delete(self):
        response=self.client.delete(reverse('stream-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


 
