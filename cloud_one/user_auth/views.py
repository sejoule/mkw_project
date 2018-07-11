from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, GroupSerializer



# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     # lookup_field = 'username'
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}
#
#     def list(self, request, *args, **kwargs):
#         request = super(viewsets.ModelViewSet, self).list(self, request, *args, **kwargs)

@api_view(['GET','POST'])
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        return Response({'data':'POST'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_specific(request, id):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({},status.HTTP_404_NOT_FOUND)
        except User.MultipleObjectsReturned:
            return Response({},status.HTTP_300_MULTIPLE_CHOICES)
    else:
        return Response({},status.HTTP_405_METHOD_NOT_ALLOWED)

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer