from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response

from movie_app.api.serializers import MovieSerializer, StreamPlatformSerializer, ReviewSerializer
from movie_app.models import Movie, Review, StreamPlatform

class MovieListMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request, *args,**kwargs)
    
class MovieDetailMixin(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

    def get(self, request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self, request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
class StreamPlatformListMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request, *args,**kwargs)
    
class StreamPlatformDetailMixin(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer

    def get(self, request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self, request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class ReviewListMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request, *args,**kwargs)
    
class ReviewDetailMixin(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    def get(self, request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self, request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    