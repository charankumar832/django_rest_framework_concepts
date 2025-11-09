from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.urls import reverse

from movie_app import models
from movie_app.api import serializers

class MovieListTestCase(APITestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='username',password='password')
        self.token,created=Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        self.stream=models.StreamPlatform.objects.create(name='netflix',about='netflix vedios',website='netflix.com')
        self.movie=models.Movie.objects.create(platform=self.stream,title='first',storyline='comedy',active=True)


    def test_moviecreate(self):
        data={
            'title':'example',
            'storyline':'example',
            'platform':self.stream.id,
            'active':True
        }
        
        response=self.client.post(reverse('movie-list'),data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_movielist(self):
        response=self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_movielist_indiviual(self):
        response=self.client.get(reverse('movie-details', args=(self.movie.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_movie_update(self):
        data={
            'title':'example',
            'storyline':'example',
            'platform':self.stream.id,
            'active':True
        }

        response=self.client.put(reverse('movie-details', args=(self.movie.id,)),data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_movie_delete(self):
        response=self.client.delete(reverse('movie-details',args=(self.movie.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


