from rest_framework import serializers
from movie_app.models import Movie


# Custom Validators: We can define our own custom validations and we can apply these to the specific feilds

def len_storyline (value):
    if len(value)<5:
        raise serializers.ValidationError("Storyline is too short..!!")
    else:
        return value

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True) 
    title=serializers.CharField(max_length=20) # Here max_length is also a validator that will validate the max length of title
    storyline=serializers.CharField(validators=[len_storyline]) #Here we are using a custom validator. So we need to assign it like this
    active=serializers.BooleanField(default=True) 
    
    # Field-Level validators: This validators will be applied to specific field. (validate_<field-name>)
    # Here in this case it is used to validate the title.

    def validate_title(self, value):
        
        if len(value)<3:
            raise serializers.ValidationEror("Name is too short..!!")
        else:
            return value
    
    # Serializer-Level Validators: Can validate multiple fields together. 
    # Here are we are validating title and storyline and checking if both are matching or not.

    def validate(self, data):

        if data['title']==data['storyline']:
            raise serializers.ValidationError("Title and Storyline should not match.")
        return data

    # This is best example. While setting password to any account, Both the passwords should match
    # def validate(self, data):
    #     if data['password']!=data['password2']:
    #         raise serializers.ValidationError("Passwords are not matching..!!")

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.storyline=validated_data.get('storyline',instance.storyline)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance
    
