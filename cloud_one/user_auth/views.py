from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer, AvatarSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UserJWTSecret
import uuid



class UserViewSet(viewsets.ViewSet):
    '''
    ViewSet for CRUD operations on the user account
    '''
    parser_classes = (MultiPartParser, FormParser)

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        pass


class UserLogoutAllView(APIView):
    '''
    Provides an APIView for logging out a user from all
    server sessions. The user's jwt secret is be changed so
    that the token becomes invalid.
    '''
    def post(self, request, *args, **kwargs):
        pk = request.data.get('id')
        try:
            user_jwt = UserJWTSecret.objects.get(user_id=pk)
            user_jwt.jwt_secret = uuid.uuid4()
            user_jwt.save()
            return Response(data={'username': user_jwt.user.username}, status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserAvatarViewSet(viewsets.ViewSet):
    '''
    ViewSet that for changing the user's profile avatar.
    It will return the user's account if successful
    '''
    parser_classes = (MultiPartParser, FormParser)

    def update(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            serializer = AvatarSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                user_serializer = UserSerializer(user)
                return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


