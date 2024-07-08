from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .utils import decode_jwt_token
# Create your views here.

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh' : str(refresh),
                'access' : str(refresh.access_token), 
            }, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class CurrentUserView(APIView):
    
    
    def get(self, request):
       token = request.data['token']
       decoded_token = decode_jwt_token(token)
       current_user = User.objects.get(id=decoded_token['user_id'])
       serializer = UserSerializer(data=current_user)
       if serializer.is_valid():
           print(serializer.data)
           return Response(serializer.data)
       return Response(serializer.errors, status.HTTP_401_UNAUTHORIZED)
                   
