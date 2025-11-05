from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movie_app.api.views import MovieVS, StreamPlatformVS, ReviewVS

router=DefaultRouter()
router.register('movie',MovieVS, basename='movies')
router.register('stream', StreamPlatformVS, basename='streams')
router.register('review', ReviewVS, basename='reviews')

urlpatterns = [
        path('', include(router.urls)),
]
