from rest_framework import viewsets
from movie_app.api.serializers import MovieSerializer, StreamPlatformSerializer, ReviewSerializer
from movie_app.models import Movie, Review, StreamPlatform

class MovieMVS(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class ReviewMVS(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

class StreamPlatformMVS(viewsets.ModelViewSet):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer