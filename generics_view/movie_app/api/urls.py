from django.urls import path
from movie_app.api.views import (MovieListGV,MovieDetailGV,StreamPlatformListGV
                                 ,StreamPlatformDetailGV,ReviewListGV,ReviewDetailGV)

urlpatterns = [
    path('list/', MovieListGV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailGV.as_view(),name='movie-detail'),
    path('stream/list/',StreamPlatformListGV.as_view(), name='stream-list'),
    path('stream/<int:pk>/',StreamPlatformDetailGV.as_view(), name='stream-detail'),
    path('review/list/',ReviewListGV.as_view(),name='review-list'),
    path('review/<int:pk>/',ReviewDetailGV.as_view(),name='review-detail'),
]
