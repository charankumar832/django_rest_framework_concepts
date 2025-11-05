from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly

from movie_app.api.serializers import MovieSerializer, StreamPlatformSerializer, ReviewSerializer
from movie_app.models import Movie, Review, StreamPlatform
from movie_app.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly

# This is only to list the reviews of particular movie

class ReviewListGV(generics.ListAPIView):
    # queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[AllowAny]

    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(pk=pk)
    

# This is to create the review for a particular movie.
# We restricted user to write only one review to a movie.
# We also added avg_rating and no of reviews fields to the movie.

class ReviewCreateGV(generics.CreateAPIView):
    # queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk=self.kwargs['pk']
        movie=Movie.objects.get(pk=pk)
        
        review_user=self.request.user
        review_queryset=Review.objects.filter(movie=movie, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie..!!")

        if movie.no_of_rating==0:
            movie.avg_rating=serializer.validated_data['rating']
        else:
            movie.avg_rating=(movie.avg_rating+serializer.validated_data['rating'])/2

        movie.no_of_rating+=1
        
        movie.save()
        serializer.save(movie=movie, review_user=review_user)

# This is to retrieve/update/destroy a particular movie
class ReviewDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsReviewUserOrReadOnly]

class MovieListGV(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    permission_classes=[IsAuthenticated]

class MovieDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    permission_classes=[IsAdminOrReadOnly]

class StreamPlatformListGV(generics.ListCreateAPIView):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer
    permission_classes=[IsAdminOrReadOnly]

class StreamPlatformDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer
    permission_classes=[IsAdminOrReadOnly]
