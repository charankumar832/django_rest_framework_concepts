from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from movie_app.api.serializers import MovieSerializer, StreamPlatformSerializer, ReviewSerializer
from movie_app.models import Movie, Review, StreamPlatform


class MovieVS(viewsets.ViewSet):
    
    def list(self,request):
        movie=Movie.objects.all()
        serializer=MovieSerializer(movie,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk):
        movie=get_object_or_404(Movie,pk=pk)
        serializer=MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self,request, pk):
        movie=get_object_or_404(Movie,pk=pk)
        serializer=MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        movie=get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformVS(viewsets.ViewSet):
    
    def list(self,request):
        movie=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(movie,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk):
        movie=get_object_or_404(StreamPlatform,pk=pk)
        serializer=StreamPlatformSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self,request, pk):
        movie=get_object_or_404(StreamPlatform,pk=pk)
        serializer=StreamPlatformSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        movie=get_object_or_404(StreamPlatform, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewVS(viewsets.ViewSet):
    
    def list(self,request):
        movie=Review.objects.all()
        serializer=ReviewSerializer(movie,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk):
        movie=get_object_or_404(Review,pk=pk)
        serializer=ReviewSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self,request, pk):
        movie=get_object_or_404(Review,pk=pk)
        serializer=ReviewSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        movie=get_object_or_404(Review, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    