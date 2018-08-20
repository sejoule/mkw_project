from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from .models import ServiceTemplate, TopologyTemplate, NodeTemplate, Version, AttributeAssignment
from .serializers import FileSerializer, ServiceTemplateSerializer, VersionSerializer, AttributeAssignmentSerializer
from user_auth.serializers import UserSerializer
from rest_framework_yaml.parsers import YAMLParser
from rest_framework.parsers import JSONParser
from rest_framework_yaml.renderers import YAMLRenderer
from mongoengine import *
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from .transformers import *
import datetime, yaml

# Create your views here.

'''
API views will be used and each required method, POST, PUT, GET, DELETE will be 
created. 
'''


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            current_user = User.objects.get(username=UserSerializer(request.user).data['username'])
            try:
                file = file_serializer.validated_data['file']
                data = yaml.load(file)
                service_template = create_service_template(data)
                service_template.clean()
                service_template.save(cascade=True)
                srv_temp_file = ServiceTemplateFile(
                    file=file,
                    template_name=service_template.name,
                    template_id=str(service_template['id']),
                    user=current_user,
                    created_date=datetime.datetime.today()
                )
                srv_temp_file.save()
            except ValidationError as e:
                return Response(e.to_dict(), status=status.HTTP_400_BAD_REQUEST)
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceTemplateViewSet(viewsets.ViewSet):
    parser_classes = (YAMLParser, JSONParser)

    def list(self, request):
        service_templates = ServiceTemplate.objects()
        serializer = ServiceTemplateSerializer(service_templates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response({'service_templates':'service_templates'}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            service_template = ServiceTemplate.objects(id=pk)
            serializer = ServiceTemplateSerializer(service_template)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def update(self, request, pk=None):
        try:
            service_template = ServiceTemplate.objects(id=pk)
            if service_template:
                serializer = ServiceTemplateSerializer(service_template, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST) #TODO might need to change this


    def create(self, request):
        data = request.data
        current_user = User.objects.get(username= UserSerializer(request.user).data['username'])
        service_template = create_service_template(data)
        try:
            service_template.clean()
            service_template.save(cascade=True)
            srv_temp_usr = ServiceTemplateFile(
                file=None,
                template_name=service_template.name,
                template_id=str(service_template['id']),
                user=current_user,
                created_date=datetime.datetime.today()
                )
            srv_temp_usr.save()
            return Response(ServiceTemplateSerializer(service_template).data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(e.to_dict(), status=status.HTTP_400_BAD_REQUEST)


class PolicyTypeViewSet(viewsets.ViewSet):
    pass

class NodeDefinitionViewSet(viewsets.ViewSet):
    pass

class InterfaceTypeViewSet(viewsets.ViewSet):
    pass

class GroupTypeViewSet(viewsets.ViewSet):
    pass

class DataTypeViewSet(viewsets.ViewSet):
    pass

class CapabilityDefinitionViewSet(viewsets.ViewSet):
    pass

class ArtifactTypeViewSet(viewsets.ViewSet):
    pass


