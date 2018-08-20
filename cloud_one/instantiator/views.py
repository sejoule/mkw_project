from django.shortcuts import render
from mongoengine import *
from tosca.models import ServiceTemplateFile, ServiceTemplate, TopologyTemplate, NodeTemplate
from user_auth.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


#NOTE: may change to id or any other unique field
def instantiate_app(request):
    template_name = request.data
    user_name = UserSerializer(request.user).data
    st_file = ServiceTemplateFile.objects.get(user__username=user_name, template_name=template_name)
    template = st_file.template_id
    service_template = ServiceTemplate(id(template))
    return Response({'status':'{} was instantiated'.format(template_name)}, status=status.HTTP_201_CREATED)
    #NOTE launch the template here.
