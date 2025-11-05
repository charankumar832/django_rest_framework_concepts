from django.urls import path
from movie_app.api.views import MovieDetailGV,MovieListGV, StreamPlatformListGV,StreamPlatformDetailGV, ReviewListGV, ReviewDetailGV, ReviewCreateGV

urlpatterns = [
    path('list/', MovieListGV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailGV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformListGV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailGV.as_view(), name='stream-detail'),
    path('review/<int:pk>/', ReviewDetailGV.as_view(), name='review-detail'),
    path('<int:pk>/review/', ReviewListGV.as_view(), name='review-list'),
    path('<int:pk>/review-create/', ReviewCreateGV.as_view(),name='review-create'),
]

