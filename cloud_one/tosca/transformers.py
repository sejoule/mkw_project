from .models import *
import re


def create_version(data):
    matchObj = re.match('^((\d+)\.(\d+)(\.(\d+)(\.(\w+)(-(\d+))))*)$',data)
    return Version(
        major_version = matchObj.group(2) if matchObj.group(2) is not None else -1,
        minor_version = matchObj.group(3) if matchObj.group(3) is not None else -1,
        fixed_version = matchObj.group(5) if matchObj.group(5) is not None else -1,
        qualifier = matchObj.group(7) if matchObj.group(7) is not None else '',
        build_version = matchObj.group(9) if matchObj.group(9) is not None else -1,
    )

#***************************************************************************************************
# type definitions

def create_credential(data):
    name = list(data.keys())[0]
    return Credential(
        protocol=data[name].get('protocol') if data[name].get('protocol') is not None else '',
        token_type = data[name].get('token_type') if data[name].get('token_type') is not None else '',
        token = data[name].get('token') if data[name].get('token') is not None else '',
        # keys = MapField(StringField(max_length=STRING_LENGTH), null=True)
        userh = data[name].get('userh') if data[name].get('userh') is not None else ''
    )

def create_repository(data):
    name = list(data.keys())[0]
    return RepositoryDefinition(
        description=data[name].get('description') if data[name].get('description') is not None else '',
        url = data[name].get('url') if data[name].get('url') is not None else '',
        credential = create_credential(data.get('credential')) if data.get('credential') is not None else ''
    )

def create_constraint(data):
    return ConstraintClause(
        operator=data.get('operator') if data.get('operator') is not None else '',
        #operands = create_operand(data) #Any or Scalar or RegExpression
    )

def create_property_definition(data):
    name = list(data.keys())[0]
    return PropertyDefinition(
        type=data[name].get('type') if data[name].get('type') is not None else '',
        description = data[name].get('description') if data[name].get('description') is not None else '',
        required = data[name].get('required') if data[name].get('required') is not None else True,
        default = data[name].get('default') if data[name].get('default') is not None else None,
        status = data[name].get('status') if data[name].get('status') is not None else '',
        constraints = [constraint for constraint in data[name].get('constraints')] if data[name].get('constraints') is not None else [],
        entry_schema = data[name].get('entry_schedma') if data[name].get('entry_schema') is not None else '',
    )

def create_artifact_type(data):
    name = list(data.keys())[0]
    return ArtifactType(
        derived_from = data[name].get('derived_from') if data[name].get('derived_from') is not None else '',
        version = create_version(data['tosca_definition_version']) if data['tosca_definition_version'] is not None else '',
        description = data[name].get('description') if data[name].get('description') is not None else '',
        mime_type = data[name].get('mime_type') if data[name].get('mime_type') is not None else '',
        file_ext = [file_ext for file_ext in data[name].get('file_ext')] if data[name].get('file_ext') is not None else [],
        properties = [create_property_definition(property_def) for property_def in data[name].get('properties')] if data[name].get('properties') is not None else [],
    )

#***************************************************************************************************
# template definitions

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
        # attributes = [create_attribute(attribute) for attribute in data[name]['attribbutes']],
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

def create_artifact(data):
    name = list(data.keys())[0]
    return ArtifactDefinition(
        type = data[name].get('type') if data[name].get('type') is not None else '',
        description = data[name].get('description') if data[name].get('description') is not None else '',
        file = data[name].get('file') if data[name].get('file') is not None else '',
        repository = data[name].get('repository') if data[name].get('repository') is not None else '',
        deploy_path = data[name].get('deploy_path') if data[name].get('deploy_path') is not None else '',
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
        artifacts = [create_artifact(artifact) for artifact in data[name].get('artifacts')] if data[name].get('artifacts') is not None else [],
        # node_filter = create_node_filter(data[name]['node_filter']),
        copy = data[name].get('copy') if data[name].get('copy') is not None else ''
    )

def create_relationship_template(data):
    name = list(data.keys())[0]
    return RelationshipTemplate(
        name=name,
        type=data[name].get('type') if data[name].get('type') is not None else '',
        description = data[name].get('description') if data[name].get('description') is not None else '',
        properties = [create_property_assignment(property_assignment) for property_assignment in data[name].get('properties')] if data[name].get('properties') is not None else [],
        # attributes = [create_attribute(attribute) for attribute in data[name]['attribbutes']],
        # interfaces = [create_interface(interface) for interface in data.get('interfaces')] if data.get('interfaces') is not None else [],
        copy = data[name].get('copy') if data[name].get('copy') is not None else ''
    )

def create_group(data):
    name = list(data.keys())[0]
    return GroupDefinition(
        type=data[name].get('type') if data[name].get('type') is not None else '',
        description=data[name].get('description') if data[name].get('description') is not None else '',
        properties=[create_property_assignment(property_assignment) for property_assignment in data[name].get('properties')] if data[name].get('properties') is not None else [],
        members = [member for member in data.get('members')] if data.get('members') is not None else [],
        # interfaces = [create_interface(interface) for interface in data.get('interfaces')] if data.get('interfaces') is not None else []
    )

def create_policy(data):
    name = list(data.keys())[0]
    return PolicyDefinition(
        type=data[name].get('type') if data[name].get('type') is not None else '',
        description=data[name].get('description') if data[name].get('description') is not None else '',
        properties=[create_property_assignment(property_assignment) for property_assignment in data[name].get('properties')] if data[name].get('properties') is not None else [],
        targets = [target for target in data.get('targets')] if data.get('targets') is not None else [],
    )

def create_topology_template(data):
    return TopologyTemplate(
        description=data.get('description') if data.get('description') is not None else '',
        # inputs = [create_input(input) for input in data['inputs']],
        node_templates = [create_node_template(node_data) for node_data in data.get('node_templates')] if data.get('node_templates') is not None else [],
        relationship_templates = [create_relationship_template(relationship_template) for relationship_template in data.get('relationship_templates')] if data.get('relationship_templates') is not None else [],
        groups = [create_group(group) for group in data.get('groups')] if data.get('groups') is not None else [],
        policies = [create_policy(policy) for policy in data.get('policies')] if data.get('policies') is not None else [],
        # outputs = [create_output(output) for output in data['outputs']],
        substitution_mappings = data.get('substitution_mappings') if data.get('substitution_mappings') is not None else ''
    )

def create_service_template(data):
    return ServiceTemplate(
        name=data.get('name') if data.get('name') is not None else '',
        tosca_definition_version = create_version(data['tosca_definition_version']),
        # meta_data = data.get('meta_data') if data.get('meta_data') is not None else '',
        # dsl_definitions = data.get('dsl_definitions') if data.get('dsl_definitions') is not None else '',
        repositories = [create_repository(repository) for repository in data.get('repositories')] if data.get('repositories') is not None else [],
        # imports = [create_import(iport) for iport in data['imports']],
        artifacts = [create_artifact_type(artifact) for artifact in data.get('artifacts')] if data.get('artifacts') is not None else [],
        # data_types = [create_data_type(data_type) for data_types in data['data_types']],
        # capability_types = [create_capability_type(capability_type) for capability_type in data['capability_types']],
        # interface_types = [create_interface_type(interface_type) for interface_type in data['interface_types']],
        # relationship_types = [create_relationship_type(relationship_type) for relationship_types in data['relationship_types']],
        # node_types = [create_node_type(node_type) for node_type in data['node_types']],
        # group_types = [create_group_type(group_type) for group_type in data['group_types']],
        # policy_types = [create_policy_type(policy_type) for policy_type in data['policy_types']],
        topology_template=create_topology_template(data.get('topology_template')) if data.get('topology_template') is not None else ''
    )

#***************************************************************************************************