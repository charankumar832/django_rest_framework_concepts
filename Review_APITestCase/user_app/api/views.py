from user_app.api.serializers import RegistrationSerializer
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

@api_view(['POST',])
@permission_classes([AllowAny])
def registration_view(request):
    serializer=RegistrationSerializer(data=request.data)
    details={}

    if serializer.is_valid():
        account=serializer.save()

        details['response']="Registration Successful"
        details['username']=account.username
        details['email']=account.username

        token,created=Token.objects.get_or_create(user=account)
        details['token']= token.key
        return Response(details, status=status.HTTP_201_CREATED)
       
    else:
        details=serializer.errors
        return Response(details, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST',])

def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

    

    


