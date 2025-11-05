from django.contrib import admin
from movie_app.models import Review,StreamPlatform,Movie

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(StreamPlatform)
