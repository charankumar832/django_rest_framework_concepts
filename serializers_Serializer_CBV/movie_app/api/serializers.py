from rest_framework import serializers
from movie_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=20)
    storyline=serializers.CharField(max_length=200)
    active=serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.storyline=validated_data.get('storyline',instance.storyline)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance
    
