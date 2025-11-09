from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from movie_app.api.serializers import MovieSerializer, StreamPlatformSerializer, ReviewSerializer
from movie_app.models import Movie, Review, StreamPlatform
from movie_app.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from movie_app.api.throttling import StreamDetailThrottle, ReviewDetailThrottle
from movie_app.api.pagination import MovieListPagination, ReviewListPagination, StreamListPagination



class MovieListGV(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    permission_classes=[IsAuthenticated]
    throttle_classes=[ScopedRateThrottle, UserRateThrottle]
    throttle_scope='movie-list'
    filter_backends=[DjangoFilterBackend] # This is for Filtering
    filterset_fields=['title', 'avg_rating']
    pagination_class=MovieListPagination

class MovieDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    permission_classes=[IsAdminOrReadOnly]
    throttle_classes=[ScopedRateThrottle, UserRateThrottle]
    throttle_scope='movie-detail'
    

class StreamPlatformListGV(generics.ListCreateAPIView):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer
    permission_classes=[IsAdminOrReadOnly]
    throttle_classes=[AnonRateThrottle, UserRateThrottle]
    filter_backends=[filters.SearchFilter] # This is for Searching
    search_fields=['=name','about','^website'] # '=' for exact match, '^' for startswith and nothing for nearby search
    pagination_class=StreamListPagination

class StreamPlatformDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer
    permission_classes=[IsAdminOrReadOnly]
    throttle_classes=[StreamDetailThrottle]
    
# This is to filter reviews with username on URL

class UserReview(generics.ListAPIView):
    #queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    def get_queryset(self):
        username=self.kwargs['username']
        return Review.objects.filter(review_user__username=username)
    
# This is to filter reviews with parameters on URL

class UserReviewParam(generics.ListAPIView):
    serializer_class=ReviewSerializer

    def get_queryset(self):
        username=self.request.query_params.get('username', None)
        return Review.objects.filter(review_user__username=username)


# This is only to list the reviews of particular movie

class ReviewListGV(generics.ListAPIView):
    # queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[AllowAny]
    filter_backends=[filters.OrderingFilter]
    ordering_fields=['rating', 'review_user__username'] # This is for Ordering
    pagination_class=ReviewListPagination

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
    throttle_classes=[UserRateThrottle, AnonRateThrottle]
    

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
    throttle_classes=[ReviewDetailThrottle]

# This is to filter reviews with username on URL

class UserReview(generics.ListAPIView):
    #queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    def get_queryset(self):
        username=self.kwargs['username']
        return Review.objects.filter(review_user__username=username)
    
# This is to filter reviews with parameters on URL

class UserReviewParam(generics.ListAPIView):
    serializer_class=ReviewSerializer

    def get_queryset(self):
        username=self.request.query_params.get('username', None)
        return Review.objects.filter(review_user__username=username)

