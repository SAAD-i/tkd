from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import CustomUser
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .utils import decode_jwt_token
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            return Response({'message': 'User already exists'}, status.HTTP_409_CONFLICT)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh' : str(refresh),
                'access' : str(refresh.access_token), 
            }, status= status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class CurrentUserView(APIView):
    
    
    def post(self, request, id):
       current_user = get_object_or_404(User, id=id)
       serializer = UserSerializer(current_user, many=False)
       if serializer:
           return Response(serializer.data, status.HTTP_200_OK)
       return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
   
class UsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
                   
