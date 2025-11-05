from rest_framework import generics
from movie_app.api.serializers import MovieSerializer, StreamPlatformSerializer, ReviewSerializer
from movie_app.models import Movie, Review, StreamPlatform


class MovieListGV(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class MovieDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class StreamPlatformListGV(generics.ListCreateAPIView):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer

class StreamPlatformDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer

class ReviewListGV(generics.ListCreateAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

class ReviewDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer