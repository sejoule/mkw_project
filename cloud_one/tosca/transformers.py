from .models import *

def create_property_assignment(data):
    name = list(data.keys())[0]
    return PropertyAssignment(
        name=name,
        value=data[name]
    )

def create_capability(data):
    name = list(data.keys())[0]
    return CapabilityAssignment(
        name=name,
        properties = [create_property_assignment(property_assignment) for property_assignment in data[name].get('properties')] if data[name].get('properties') is not None else [],
        # attributes = ListField(AttributeAssignment())
    )

def create_requirement_assignment(data):
    name = list(data.keys())[0]
    return RequirementAssignment(
        name=name,
        capability = data[name]['capability'] if data[name]['capability'] is not None else '',
        node = data[name]['node'] if data[name]['node'] is not None else '',
        relationship = data[name]['relationship'] if data[name]['relationship'] is not None else ''
        # node_filter = create_nodefilter() TODO: complete this
    )

def create_node_template(data):
    name = list(data.keys())[0]
    return NodeTemplate(
        name=name,
        type=data[name].get('type') if data[name].get('type') is not None else '',
        description=data[name].get('description') if data[name].get('description') is not None else '',
        # directives = [StringField(null=False, max_length=STRING_LENGTH)],
        properties = [create_property_assignment(property_assignment) for property_assignment in data[name].get('properties')] if data[name].get('properties') is not None else [],
        # attributes = [create_attribute(attribute) for attribute in data[name]['attribbutes']],
        requirements = [create_requirement_assignment(requirement) for requirement in data[name]['requirements']] if data[name].get('requirements') is not None else [],
        capabilities = [create_capability(capability) for capability in data[name].get('capabilities')] if data[name].get('capabilities') is not None else [],
        # interfaces = [create_interface(interface) for interface in data[name]['interfaces']],
        # artifacts = [create_artifact(artifact) for artifact in data[name]['artifacts']],
        # node_filter = create_node_filter(data[name]['node_filter']),
        copy = data[name].get('copy') if data[name].get('description') is not None else ''
    )

def create_topology_template(data):
    return TopologyTemplate(
        description=data.get('description') if data.get('description') is not None else '',
        # inputs = [create_input(input) for input in data['inputs']],
        node_templates = [create_node_template(node_data) for node_data in data.get('node_templates')] if data.get('node_templates') is not None else [],
        # relationship_templates = [create_relationship_template(relationship_template) for relationship_template in data['relationship_templates']],
        # groups = [create_group(group) for group in data['groups']],
        # policies = [create_policy(policy) for policy in data['policies']],
        # outputs = [create_output(output) for output in data['outputs']],
        substitution_mappings = data.get('substitution_mappings') if data.get('substitution_mappings') is not None else ''
    )

def create_service_template(data):
    return ServiceTemplate(
        name=data.get('name') if data.get('name') is not None else '',
        # tosca_definition_version = create_version(data['tosca_definition_version']),
        # meta_data = data.get('meta_data') if data.get('meta_data') is not None else '',
        # dsl_definitions = data.get('dsl_definitions') if data.get('dsl_definitions') is not None else '',
        # repositories = [create_repositories(repository) for repository in data['repositories']],
        # imports = [create_import(iport) for iport in data['imports']],
        # artifacts = [create_artifact(artifact) for artifact in data['artifacts']],
        # data_types = [create_data_type(data_type) for data_types in data['data_types']],
        # capability_types = [create_capability_type(capability_type) for capability_type in data['capability_types']],
        # interface_types = [create_interface_type(interface_type) for interface_type in data['interface_types']],
        # relationship_types = [create_relationship_type(relationship_type) for relationship_types in data['relationship_types']],
        # node_types = [create_node_type(node_type) for node_type in data['node_types']],
        # group_types = [create_group_type(group_type) for group_type in data['group_types']],
        # policy_types = [create_policy_type(policy_type) for policy_type in data['policy_types']],
        topology_template=create_topology_template(data.get('topology_template'))
    )
