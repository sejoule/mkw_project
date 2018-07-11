from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import ServiceTemplate, TopologyTemplate, NodeTemplate, RelationshipTemplate, ArtifactType, ArtifactDefinition, \
    DataType, CapabilityType, CapabilityDefinition, Version, Credential, RelationshipType, PolicyType, PolicyDefinition, GroupDefinition, \
    AttributeAssignment, CapabilityAssignment, RequirementAssignment, ConstraintClause, ImportDefinition, InterfaceType, \
    InterfaceDefinition, PropertyAssignment, OperationDefinition, RepositoryDefinition, NodeType, GroupType


class VersionSerializer(DocumentSerializer):
    class Meta:
        model = Version
        fields = (
            'major_version',
            'minor_version',
            'fixed_version',
            'qualifier',
            'build_version'
        )

class CredentialSerializer(DocumentSerializer):
    class Meta:
        model = Credential
        fields = (
            'protocol',
            'token_type',
            'token',
            'keys',
            'userh'
        )


class NodeTemplateSerializer(DocumentSerializer):
    class Meta:
        model = NodeTemplate
        fields = (
            'name',
            'type',
            'description',
            'directives',
            'properties',
            'attributes',
            'requirements',
            'capabilities',
            'interfaces',
            'artifacts',
            'node_filter',
            'copy'
        )

class RelationshipTemplateSerializer(DocumentSerializer):
    class Meta:
        model = RelationshipTemplate
        fields = (
            'name',
            'type',
            'description',
            'properties',
            'attributes',
            'interfaces',
            'copy'
        )

class ArtifactTypeSerializer(DocumentSerializer):
    class Meta:
        model = ArtifactType
        fields = (
            'name',
            'derived_from',
            'version',
            'description',
            'mime_type',
            'file_ext',
            'properties'
        )

class ArtifactDefinitionSerializer(DocumentSerializer):
    class Meta:
        model = ArtifactDefinition
        fields = (
            'name',
            'type',
            'file',
            'repository',
            'description',
            'deploy_path'
        )

class RepositoryDefinitionSerializer(DocumentSerializer):
    class Meta:
        model = RepositoryDefinition
        credential = CredentialSerializer
        fields = (
            'name',
            'repository',
            'url',
            'credential'
        )


class DataTypeSerializer(DocumentSerializer):
    class Meta:
        model = DataType
        fields = (
            'name',
            'type',
            'derived_from',
            'version',
            'description',
            'constraints',
            'properties'
        )

class CapabilityDefinitionSerializer(DocumentSerializer):
    class Meta:
        model = CapabilityDefinition
        fields = (
            'name',
            'type',
            'description',
            'properties',
            'attributes',
            'valid_source_types',
            'occurrences'
        )

class CapabilityTypeSerializer(DocumentSerializer):
    class Meta:
        model = CapabilityType
        fields = (
            'name',
            # 'type',
            'derived_from'
            'description',
            'properties',
            'attributes',
            'valid_source_types'
        )

class NodeTypeSerializer(DocumentSerializer):
    class Meta:
        model = NodeType
        fields = (
            'name',
            'derived_from',
            'version',
            'description',
            'properties',
            'attributes',
            'requirements',
            'capabilities',
            'interfaces',
            'artifacts'
        )

class NodeTemplateSerializer(DocumentSerializer):
    class Meta:
        model = NodeTemplate
        fields = (
            'name',
            'type',
            'description',
            'directives',
            'properties',
            'attributes',
            'requirements',
            'capabilities',
            'interfaces',
            'artifacts',
            'node_filter',
            'copy'
        )

class RelationshipTemplateSerializer(DocumentSerializer):
    class Meta:
        model = RelationshipTemplate
        fields = (
            'name',
            'description',
            'url',
            'credential'
        )

class RelationshipTypeSerializer(DocumentSerializer):
    class Meta:
        model = RelationshipType
        fields = (
            'name',
            'derived_from',
            'version',
            'description',
            'properties',
            'attributes',
            'interfaces',
            'valid_target_types'
        )

class PolicyTypeSerializer(DocumentSerializer):
    class Meta:
        model = PolicyType
        fields = (
            'name',
            'derived_from',
            'version',
            'description',
            'properties',
            'targets',
        )

class PolicyDefinitionSerializer(DocumentSerializer):
    class Meta:
        model = PolicyDefinition
        fields = (
            'name',
            'type',
            'description',
            'properties',
            'targets'
        )

class GroupTypeSerializer(DocumentSerializer):
    class Meta:
        model = GroupType
        fields = (
            'name',
            'derived_from',
            'version',
            'description',
            'properties',
            'members',
            'interfaces'
        )


class GroupDefinitionSerializer(DocumentSerializer):
    class Meta:
        model = GroupDefinition
        fields = (
            'name',
            'type',
            'description',
            'properties',
            'members',
            'interfaces'
        )


class PropertyAssignmentSerializer(DocumentSerializer):
    class Meta:
        model = CapabilityDefinition
        fields = (
            'name',
            'value'
        )

class AttributeAssignmentSerializer(DocumentSerializer):

    class Meta:
        model = AttributeAssignment
        fields = (
            'name',
            'value'
        )

class CapabilityAssignmentSerializer(DocumentSerializer):
    class Meta:
        model = CapabilityAssignment
        fields = (
            'name',
            'properties',
            'attributes'
        )

class RequirementAssignmentSerializer(DocumentSerializer):
    class Meta:
        model = RequirementAssignment
        fields = (
            'name',
            'capability',
            'node',
            'relationship',
            'node_filter'
        )


class ConstraintClauseSerializer(DocumentSerializer):
    class Meta:
        model = ConstraintClause
        fields = (
            'operator',
            'operands'
        )


class ImportDefinitionSerializer(DocumentSerializer):
    class Meta:
        model = ImportDefinition
        fields = (
            'file',
            'repository',
            'namespace_uri',
            'namespace_prefix'
        )


class InterfaceTypeSerializer(DocumentSerializer):
    class Meta:
        model = InterfaceType
        fields = (
            'name',
            'derived_from',
            'version',
            'description',
            'inputs'
        )


class InterfaceDefinitionSerializer(DocumentSerializer):
    class Meta:
        model = InterfaceDefinition
        fields = (
            'name',
            'type',
            'inputs'
        )

class PropertyAssignemntSerializer(DocumentSerializer):
    class Meta:
        model = PropertyAssignment
        fields = (
            'name',
            'value'
        )


class OperationDefinitionSerializer(DocumentSerializer):
    class Meta:
        model = OperationDefinition
        fields = (
            'name',
            'description',
            'implementation',
            'inputs'
        )


class TopologyTemplateSerializer(DocumentSerializer):
    class Meta:
        model = TopologyTemplate
        fields = (
            'description',
            'inputs',
            'node_templates',
            'relationship_templates',
            'groups',
            'policies',
            'outputs',
            'substitution_mappings'
        )


class ServiceTemplateSerializer(DocumentSerializer):
    class Meta:
        model = ServiceTemplate
        tosca_definition_version = VersionSerializer()
        repository = RepositoryDefinitionSerializer()
        imports = ImportDefinitionSerializer()
        artifacts = ArtifactTypeSerializer()
        data_types = DataTypeSerializer()
        capability_types = CapabilityTypeSerializer()
        interface_types = InterfaceTypeSerializer()
        relationhsip_types = RelationshipTypeSerializer()
        node_types = NodeTypeSerializer()
        group_types = GroupTypeSerializer()
        policy_types = PolicyTypeSerializer()
        topology_template = TopologyTemplateSerializer
        fields = (
            'tosca_definition_version',
            'meta_data',
            'description',
            'dsl_definitions',
            'repositories',
            'imports',
            'artifacts',
            'data_types',
            'capability_types',
            'interface_types',
            'relationship_types',
            'node_types',
            'group_types',
            'policy_types',
            'topology_template'
        )