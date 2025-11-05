from django.urls import path
from movie_app.api.views import MovieListMixin,MovieDetailMixin,StreamPlatformListMixin,StreamPlatformDetailMixin,ReviewListMixin,ReviewDetailMixin

urlpatterns = [
    path('list/', MovieListMixin.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailMixin.as_view(),name='movie-detail'),
    path('stream/list/',StreamPlatformListMixin.as_view(), name='stream-list'),
    path('stream/<int:pk>/',StreamPlatformDetailMixin.as_view(), name='stream-detail'),
    path('review/list/',ReviewListMixin.as_view(),name='review-list'),
    path('review/<int:pk>/',ReviewDetailMixin.as_view(),name='review-detail'),
]
