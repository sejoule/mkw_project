
from tosca.metamodels import Version, DataType , string #, ArtifactType, description, string
# Create your models here.
from django.db import models

class tosca_versions(Version):
    pass


class tosca_datatypes_root(DataType):
    pass
#     derived_from = ''
#     description = ''
#
#
# class tosca_datatypes_credential(tosca_datatypes_root):
#         protocol: string,
#         token_type =  string,
#         token = string,
#         keys = map,
#         userh = string

# class tosca_datatypes_network_networkinfo(tosca_datatypes_root):
#     'network_name': string,
#     'network_id': string,
#     'network_address': [string]
#
#
# class tosca_datatypes_network_portinfo(tosca_datatypes_root):
#     'protocol': string,
#     'token_type': string,
#     'token': string,
#     'keys': map(to=string),
#     'userh': string
#
# class tosca_datatypes_network_portdef(DataType):
#     #Need to fix this
#
#
# class tosca_datatypes_network_portspec(tosca_datatypes_root):
#     'protocol': string(default='tcp'),
#     'source': tosca_datatypes_network_portdef(validators=[MinValueValidator(1), MaxValueValidator(65536)]),
#     'source_range': range,
#     'target': tosca_datatypes_network_portdef(validators=[MinValueValidator(1), MaxValueValidator(65536)]),
#     'target_range': range
#
# #********************************************************************************************************
# # Artifact types
#
# class tosca_artifacts_root(ArtifactType):
#     description = description
#
# class tosca_artifacts_file(tosca_artifacts_root):
#
# class tosca_artifacts_deployment(tosca_artifacts_root):
#
# class tosca_artifacts_deployment_image(tosca_artifacts_deployment):
#
# class tosca_artifacts_deployment_image_vm(tosca_artifacts_deployment_image):
#
# #********************************************************************************************************
# # Implementation types
#
# class tosca_artifacts_implementation(tosca_artifacts_root):
#
# class tosca_artifacts_implementation_bash(tosca_artifacts_implementation):
#
# #********************************************************************************************************
# # Capability types
#
# class tosca_capability_root(CapabilityType):
#     description = description
#
# class tosca_capability_node(tosca_capability_root):
#
# class tosca_capability_container(tosca_capability_root):
#     'num_cpus': integer(validators=[MinValueValidator(1)]),
#     'cpu_frequency': ScalarUnit_frequency, #add validator
#     'disk_size': ScalarUnit_size,
#     'mem_size': ScalarUnit_size
#
# class tosca_capability_endpoint(tosca_capability_root)
#     'properties': {
#         'protocol': string,
#         'port': tosca_datatypes_network_portdef,
#         'secure': boolean,
#         'url_path': string,
#         'port_name': string,
#         'network_name': string,
#         'initiator': string,
#         'ports': map(to= tosca_datatypes_network_portspec)
#     },
#     'attributes': {
#         'ip_address': string
#     }
#
#
