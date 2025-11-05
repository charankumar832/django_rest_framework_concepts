from rest_framework import serializers
from movie_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):

    len_title=serializers.SerializerMethodField()

    class Meta:
        model=Movie
        fields="__all__"  # configure all the feilds in the Model(Movie)

        # fields=['id','title','storyline','active'] only mentioned fields wil be configured.
        # exclude=['active'] Only this field will be excluded and other fields will be configured.
    
    def get_len_title(self, object):
        length=len(object.title)
        return length
    
    def validate_title(self,value):
        if len(value)<3:
            raise serializers.ValidationError("Name is too short..!!")
        return value
    
