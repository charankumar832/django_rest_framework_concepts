from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from user_app.api.serializers import RegistrationSerializer

@api_view(['POST',])
@permission_classes([AllowAny]) 
def registration_view(request):
    
    if request.method =='POST':
        serializer=RegistrationSerializer(data=request.data)

        data={}

        if serializer.is_valid():

            account=serializer.save()

            data['response']="Registration Successful"
            data['username']=account.username
            data['email']=account.email

            token, created=Token.objects.get_or_create(user=account)
            data['token']=token.key

        else:
            data=serializer.errors

        return Response(data)

@api_view(['POST']) 

def logout_view(request):

    if request.method== 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

        

