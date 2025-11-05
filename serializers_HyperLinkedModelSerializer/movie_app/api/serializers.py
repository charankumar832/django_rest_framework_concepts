from rest_framework import serializers
from movie_app.models import Movie

# When compared to ModelSerializer everything will be same. Same syntax.
# We need to add context={'request':request} in every view(where we have given serializer=MoviSerializer(movie,context:...))
# But only major change is in browser this will show hyperlink(URL) instead of id.


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    len_title=serializers.SerializerMethodField()

    class Meta:
        model=Movie
        fields="__all__"  
    

    def get_len_title(self, object):
        length=len(object.title)
        return length
    
    def validate_title(self,value):
        if len(value)<3:
            raise serializers.ValidationError("Name is too short..!!")
        return value
    
