from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from .models import ServiceTemplate, Version, AttributeAssignment
from .serializers import ServiceTemplateSerializer, VersionSerializer, AttributeAssignmentSerializer
from rest_framework_yaml.parsers import YAMLParser
from rest_framework_yaml.renderers import YAMLRenderer


# Create your views here.

'''
API views will be used and each required method, POST, PUT, GET, DELETE will be 
created. 
'''
class Attribute(APIView):
    def get_object(self, name):
        return AttributeAssignment.objects(name=name).first()

    def get(self, request, name, format=None):
        attr = self.get_object(name)
        if attr:
            serializer = AttributeAssignmentSerializer(attr)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, name, format=None):
        attr = self.get_object(name)
        if attr:
            serializer = AttributeAssignmentSerializer(attr, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        serializer = AttributeAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# def service_template_list(request):
#     if request.method == 'GET':
#         service_templates = ServiceTemplate.objects()
#         serializer = ServiceTemplateSerializer(service_templates, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#         return Response({},status.HTTP_405_METHOD_NOT_ALLOWED)
#
# @api_view(['GET','POST'])
# def service_template(request, name):
#     if request.method == 'GET':
#         service_template = ServiceTemplate.objects(name = name).first()
#         serializer = ServiceTemplateSerializer(service_template)
#         return Response(serializer.data, status= status.HTTP_200_OK)
#     else:
#         return Response({}, status.HTTP_405_METHOD_NOT_ALLOWED)

