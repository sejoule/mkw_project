# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
# from metamodels import ArtifactType, DataType, CapabilityType, ScalarUnit_frequency, string, map, integer, boolean
#
# #********************************************************************************************************
# # Datatypes
#
# tosca_datatypes_root = type('tosca.datatypes.root', (DataType,), {})
#
# tosca_datatypes_credential = type('tosca.datatypes.credential', (tosca_datatypes_root,), {
#     'protocol': string,
#     'token_type': string,
#     'token': string,
#     'keys': map(to=string),
#     'userh': string
# })
#
# tosca_datatypes_network_networkinfo = type('tosca.datatypes.network.networkinfo', (tosca_datatypes_root,), {
#     'network_name': string,
#     'network_id': string,
#     'network_address': [string]
# })
#
# tosca_datatypes_network_portinfo = type('tosca.datatypes.network.portinfo', (tosca_datatypes_root,), {
#     'protocol': string,
#     'token_type': string,
#     'token': string,
#     'keys': map(to=string),
#     'userh': string
# })
#
# tosca_datatypes_network_portdef = type('tosca.datatypes.network.portdef', (DataType,), {
#     #Need to fix this
# })
#
# tosca_datatypes_network_portspec = type('tosca.datatypes.network.portspec', (tosca_datatypes_root,), {
#     'protocol': string(default='tcp'),
#     'source': tosca_datatypes_network_portdef(validators=[MinValueValidator(1), MaxValueValidator(65536)]),
#     'source_range': range,
#     'target': tosca_datatypes_network_portdef(validators=[MinValueValidator(1), MaxValueValidator(65536)]),
#     'target_range': range
# })
#
# #********************************************************************************************************
# # Artifact types
#
# tosca_artifacts_root = type('tosca.artifacts.root', (ArtifactType,), {})
#
# tosca_artifacts_file = type('tosca.artifacts.file', (tosca_artifacts_root,), {})
#
# tosca_artifacts_deployment = type('tosca.artifacts.deployment', (tosca_artifacts_root,), {})
#
# tosca_artifacts_deployment_image = type('tosca.artifacts.deployment.image', (tosca_artifacts_deployment,), {})
#
# tosca_artifacts_deployment_image_vm = type('tosca.artifacts.deployment.image.vm', (tosca_artifacts_deployment_image,), {})
#
# #********************************************************************************************************
# # Implementation types
#
# tosca_artifacts_implementation = type('tosca.artifacts.implementation', (tosca_artifacts_root,), {})
#
# tosca_artifacts_implementation_bash = type('tosca.artifacts.implementation.bash', (tosca_artifacts_implementation,), {})
#
# #********************************************************************************************************
# # Capability types
#
# tosca_capability_root = type('tosca.capability.root', (CapabilityType,), {})
#
# tosca_capability_node = type('tosca.capability.node', (tosca_capability_root,), {})
#
# tosca_capability_container = type('tosca.capability.container', (tosca_capability_root,), {
#     'num_cpus': integer(validators=[MinValueValidator(1)]),
#     'cpu_frequency': ScalarUnit_frequency, #add validator
#     'disk_size': ScalarUnit_size,
#     'mem_size': ScalarUnit_size
# })
#
# tosca_capability_endpoint = type('tosca.capability.endpoint', (tosca_capability_root,), {
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
# })
#
