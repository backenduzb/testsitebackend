from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, LoginSerializer, UserRegisterSerializer, ClassSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import User, Class
from rest_framework import status

class CutomLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        response = Response({'message':'Login muvofaqiyatli!'}, status=200)

        response.set_cookie(
            key='access_token',
            value=data['access'],
            httponly=False,
            secure=False,
            samesite="none",
            max_age=604800,
            domain="vercel.app"
        )
        response.set_cookie(
            key='refresh_token',
            value=data['refresh'],
            httponly=False,
            secure=False,
            samesite="none",
            max_age=604800,
            domain="vercel.app"
        )


        return response

class LogoutView(APIView):
    
    def post(self, request):
        refresh = request.COOKIES.get('refresh_token')

        if not refresh:
            return Response(
                {'message': "Refresh token topilmadi."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh)
            token.blacklist()
        except TokenError:
            return Response(
                {'message': "Token allaqachon yaroqsiz."},
                status=status.HTTP_400_BAD_REQUEST
            )

        response = Response(
            {'message': 'Logout muvaffaqiyatli yakunlandi.'},
            status=status.HTTP_200_OK
        )

        response.delete_cookie(
            'access_token',
            path='/',
            samesite='Lax'
        )
        response.delete_cookie(
            'refresh_token',
            path='/',
            samesite='Lax'
        )

        return response


class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(
            serializer.data,
            status=200
        )

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = serializer.save()

        response = Response(UserSerializer(user).data, status=201)

        return response
    

class GetUserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        
        return Response(
            {'data':serializer.data},
            status=200
        )
