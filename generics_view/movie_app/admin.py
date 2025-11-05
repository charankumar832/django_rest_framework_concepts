from django.contrib import admin
from movie_app.models import Movie,Review,StreamPlatform

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(StreamPlatform)