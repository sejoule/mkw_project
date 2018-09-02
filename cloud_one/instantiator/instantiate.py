from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.base import NodeImage


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
    template = st_file.template_ref
    return Response({'status':'{} was instantiated'.format(template_name)}, status=status.HTTP_201_CREATED)
    #NOTE launch the template here.

def create_node(itype):
	AWS_ACCESS_KEY_ID = 'AKIAJ5C7RLCLY663JKKA'
	AWS_SECRET_ACCESS_KEY = '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'
	AMI_ID = 'ami-02c8553c261eda3bd'
	SIZE_ID = itype
	AWS_REGION = 'ap-northeast-2'
	
	EC2Driver = get_driver(Provider.EC2)
	driver = EC2Driver(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, region=AWS_REGION)
	
	sizes = driver.list_sizes()
	size = [s for s in sizes if s.id == itype][0]
	
	image = NodeImage(id=AMI_ID, name=None, driver=driver)
	
	node = driver.create_node(name='test-node', image=image, size=size)

def getMongo(name):
	st = ServiceTemplate.objects.get(name = name)
	instance_type =  st.topology_template.node_templates[0].properties[0].value
	return instance_type

def instantiate():
	i_type = getMongo("mj_template")
	create_node(i_type)
