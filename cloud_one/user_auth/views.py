from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, AvatarSerializer
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser



class UserViewSet(viewsets.ViewSet):

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


class UserAvatarViewSet(viewsets.ViewSet):
    parser_classes = (MultiPartParser, FormParser)
    # def retrieve(self, request, pk=None):
    #     try:
    #         user = User.objects.get(id=pk)
    #         serializer = AvatarSerializer(user)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except User.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            serializer = AvatarSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# class AvatarUploadView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     def put(self, request, *args, **kwargs):
#         avatar_serializer = AvatarSerializer(data=request.data)
#         if avatar_serializer.is_valid():
#             current_user = User.objects.get(username=UserSerializer(request.user).data['username'])
#             try:
#                 avatar = avatar_serializer.validated_data['file']
#                 avatar_file = AvatarFile(
#                     file=avatar,
#                     user=current_user,
#                     created_date=datetime.datetime.today()
#                 )
#                 avatar_file.save()
#             except ValidationError as e:
#                 return Response(e.to_dict(), status=status.HTTP_400_BAD_REQUEST)
#             return Response({'user': UserSerializer(current_user).data, 'url': avatar_file.file.url}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(avatar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
