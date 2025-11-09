from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.urls import reverse

from movie_app import models
from movie_app.api import serializers

class ReviewTestCase(APITestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='username',password='password')
        self.token, created=Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

        self.stream=models.StreamPlatform.objects.create(name='netflix',about='netflix vedios',website='netflix.com')
        self.movie=models.Movie.objects.create(title='example',storyline='example-storyline',active=True,platform=self.stream)
        self.movie2=models.Movie.objects.create(title='example1', storyline='example-storline', active=True, platform=self.stream)
        self.review=models.Review.objects.create(review_user=self.user,rating=4,description='good',movie=self.movie2, active=True)

    def test_review_create(self):
        data={
            'review_user':self.user.id,
            'rating':4,
            'description':'Great',
            'movie':self.movie.id,
            'active':True
        }
        
        response=self.client.post(reverse('review-create', args=(self.movie.id, )),data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_review_create_unauthorized(self):
        data={
            'review_user':self.user.id,
            'rating':4,
            'description':'Great',
            'movie':self.movie.id,
            'active':True
        }
        self.client.force_authenticate(user=None)
        response=self.client.post(reverse('review-create', args=(self.movie.id,)),data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data={
            'review_user':self.user.id,
            'rating':4,
            'description':'Great-updated',
            'movie':self.movie.id,
            'active':True
        }

        response=self.client.put(reverse('review-detail', args=(self.review.id,)),data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response=self.client.get(reverse('review-list', args=(self.movie.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_indiviual(self):
        response=self.client.get(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_user(self):
        resposne=self.client.get('/movie/review/?username'+self.user.username)
        self.assertEqual(resposne.status_code, status.HTTP_200_OK)

    def test_review_delete(self):
        response=self.client.delete(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)