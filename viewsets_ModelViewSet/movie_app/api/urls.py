from django.urls import path,include
from rest_framework.routers import DefaultRouter
from movie_app.api.views import MovieMVS, ReviewMVS, StreamPlatformMVS

router=DefaultRouter()
router.register('movie', MovieMVS, basename='movies')
router.register('review', ReviewMVS, basename='reviews')
router.register('stream', StreamPlatformMVS, basename='platforms')

urlpatterns = [
    path('', include(router.urls)),
]

