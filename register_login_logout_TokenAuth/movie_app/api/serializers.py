from rest_framework import serializers
from movie_app.models import Movie, Review,StreamPlatform


class ReviewSerializer(serializers.ModelSerializer): 

    review_user=serializers.StringRelatedField(read_only=True)
       
    class Meta:
        model=Review
        fields="__all__"


class MovieSerializer(serializers.ModelSerializer):

    reviews=ReviewSerializer(many=True, read_only=True)

    class Meta:
        model=Movie
        fields="__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):

    movie=MovieSerializer(many=True, read_only=True)

    class Meta:
        model=StreamPlatform
        fields="__all__"

