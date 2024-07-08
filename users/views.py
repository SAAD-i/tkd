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
        user = get_object_or_404(User, email=email)
        if user:
            return Response({'message':'User already exsits'},status.HTTP_406_NOT_ACCEPTABLE)
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
    
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
       token = request.data['token']
       decoded_token = decode_jwt_token(token)
       current_user = get_object_or_404(User, id=decoded_token['user_id'])
       data = {
           'username' : current_user.username,
           'email':current_user.email,
       }
       return Response(data)
   
class UsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
                   
