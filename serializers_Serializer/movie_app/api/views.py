from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from movie_app.models import Movie
from movie_app.api.serializers import MovieSerializer

@api_view(['GET','POST'])
def movie_list(request):

    # this is used to access whole movie list(get) and add new movie detials(post).   
    if request.method=='GET':
        movie=Movie.objects.all()
        serializer=MovieSerializer(movie,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['GET','PUT','DELETE'])

def movie_details(request,pk):
    
    # this is to access indiviual movie and it ensures that the accessing movie already exists
    try:
        movie=Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=MovieSerializer(movie,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    elif request.method=='DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

        

        
        

    
    