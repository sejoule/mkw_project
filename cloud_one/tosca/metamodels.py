from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import operator
# from tosca.metamodels import CapabilityType, PropertyAssignment, AttributeAssignment, propertyValue, attributeValue
from tosca.validators import IsOfValidator

#******************************************************************
# CONSTS

STRING_LENGTH    = 1000
DESC_LENGTH      = 2000


#******************************************************************
# Referenced Data types
string       = models.CharField
integer      = models.IntegerField
float        = models.FloatField
boolean      = models.BooleanField
timestamp    = models.DateTimeField
list         = models.ForeignKey
map          = models.ManyToManyField
null         = models.NOT_PROVIDED
#******************************************************************

UNBOUNDED     = 10000000000000 #very large number but will change later
scalar      = integer(default=0) or float(default=0) or boolean(default=True) or string(default='')
description = string#(max_length=1000)

url         = models.URLField

#******************************************************************
# operators

# constraint_clauses = {
equal              = operator.eq
greater_than       = operator.gt
greater_or_equal   = operator.ge
less_than          = operator.lt
less_or_equal      = operator.le
in_range           = operator.contains

constraint_clause = equal or greater_than or greater_or_equal or less_than or less_or_equal or in_range

# Need to extend
# valid_values        = operator.contains
# length              = validators.
# min_length
# max_length
# pattern

propertyValue = attributeValue = string or integer or float or boolean or list or map or null
# attributeValue = (
#     string,
#     integer,
#     float,
#     boolean,
#     list,
#     map,
#     null
# )

any = string or integer or float or  boolean or  timestamp or  list or  map or  null or  description or  constraint_clause
    # Version,
    # Range,
    # ScalarUnit,
    # PropertyFilterDefinition,
    # NodeFilterDefinition,
    # RepositoryDefinition,
    # ArtifactDefinition,
    # ImportDefinition,
    # PropertyDefinition,



Version = type('version', (models.Model,), {
    '__module__'   : 'tosca',
    'major_version': integer(default=0, validators=[MinValueValidator(0)]),
    'minor_version': integer(default=0, validators=[MinValueValidator(0)]),
    'fixed_version': integer(null=True, validators=[MinValueValidator(0)]),
    'qualifier'    : string(null= True, max_length= STRING_LENGTH),
    'build_version': integer(null=True, validators=[MinValueValidator(0)])
})

Range = type('range', (models.Model,), {
    '__module__'   : 'tosca',
    'lower_bound': integer(default=0),
    'upper_bound': integer(default=UNBOUNDED)
})

ScalarUnit = type('scalar-unit', (models.Model,), {
    '__module__': 'tosca',
    'scalar': scalar,
    'unit': string(default='', max_length=10) # Fix later
})

ScalarUnit_frequency = type('scalar-unit.frequency', (ScalarUnit,), {
    '__module__': 'tosca',
    'unit': 'Hz' or 'kHz' or 'Mhz' or 'GHz'})

ScalarUnit_size = type('scalar-unit.size', (ScalarUnit,), {
    '__module__': 'tosca',
    'unit': 'B' or 'kB' or 'KiB' or 'MB'or 'MiB' or 'GB' or 'GiB' or 'TB' or 'TiB'})

ScalarUnit_time = type('scalar-unit.time', (ScalarUnit,), {
    '__module__': 'tosca',
    'unit': 'd' or 'h' or 'm' or 's'or 'ms' or 'us' or 'ns'})

State = type('state', (models.Model,), {
    '__module__': 'tosca',
    'value': string(default='', max_length=STRING_LENGTH),
    'transitional': boolean(default=True)
})

Credential = type('credential', (models.Model,), {
    '__module__': 'tosca',
    'protocol': string(max_length=STRING_LENGTH, null= True),
    'token_type': string(max_length=STRING_LENGTH, null= False, default='password'),
    'token': string(max_length=STRING_LENGTH, null= False, default=''),
    'keys': map,
    'userh': string(max_length=STRING_LENGTH, null= True)
})

PropertyFilterDefinition = type('PropertyFilterDefinition', (models.Model,), {
    '__module__': 'tosca',
    'property_name': string(max_length=1000, null=False, default=''), # models.CharField(max_length=255),
    'property_constraint_clause': constraint_clause
})

NodeFilterDefinition = type('NodeDefinitionFilter', (models.Model,), {
    '__module__': 'tosca',
    'properties': list,#(to= PropertyFilterDefinition, on_delete=models.SET(None)),
    'capabilities':list#(to= string, on_delete=models.SET(None)) #NOTE this are capability names or capability type names
})

RepositoryDefinition = type('RepositoryDefinition', (models.Model,), {
    '__module__': 'tosca',
    'description': description(max_length=DESC_LENGTH, null= True),
    'url': url(null= False, default=''),
    'credential': Credential(),
})

ArtifactDefinition = type('ArtifactDefinition', (models.Model,), {
    '__module__': 'tosca',
    'type': string(max_length=STRING_LENGTH, null= False, default=''),
    'file': string(max_length=STRING_LENGTH, null= False, default=''),
    'repository':string(null= True, max_length=STRING_LENGTH),
    'description': description(max_length=1000, null= True),
    'deploy_path': string(null= True, max_length=STRING_LENGTH),
})

ImportDefinition = type('ImportDefinition', (models.Model,), {
    '__module__': 'tosca',
    'file': string(max_length=STRING_LENGTH, null=False, default=''),
    'repository':string(max_length=STRING_LENGTH, null= True),
    'namespace_uri': string(max_length=STRING_LENGTH, null= True),
    'namespace_prefix': string(max_length=STRING_LENGTH, null= True),
})

PropertyDefinition = type('PropertyDefinition', (models.Model,), {
    '__module__': 'tosca',
    'type': string(max_length=STRING_LENGTH, null= False, default=''),
    'description': description(max_length=DESC_LENGTH, null=True),
    'required': boolean(default= True),
    'default': any,
    'status': string(max_length=STRING_LENGTH, null= True),
    'constraints': list,#(to=constraint_clause),
    'entry_schema': string(max_length=STRING_LENGTH, null= True),
})

AttributeDefinition = type('AttributeDefinition', (models.Model,), {
    '__module__': 'tosca',
    'type': string(max_length=STRING_LENGTH, null= False, default=''),
    'description': description(max_length= DESC_LENGTH, null=True),
    'default': any,
    'status': string(max_length=STRING_LENGTH, null= True),
    'entry_schema': string(max_length=STRING_LENGTH, null= True),
})

PropertyAssignment = type('PropertyAssignment', (models.Model,), {
    '__module__': 'tosca',
    'property_name': string(max_length=STRING_LENGTH, null= False, default=''),
    'value': propertyValue #or propertyValueExpression
})

AttributeAssignment = type('AttributeAssignment', (models.Model,), {
    '__module__': 'tosca',
    'attribute_name': string(max_length=STRING_LENGTH, null= False, default=''), #(to=PropertyAssignment),
    'value': attributeValue #or attributeValueExpression
})


ParameterDefinition = type('ParameterDefinition', (models.Model,), {
    '__module__': 'tosca',
    'type': string(max_length=STRING_LENGTH, null= True),
    'value': any
})

OperationDefinition = type('OperationDefinition', (models.Model,), {
    '__module__': 'tosca',
    'description': description(max_length= DESC_LENGTH, null= True),
    'implementation': string(max_length=STRING_LENGTH, null= True) or {
        'primary': string(max_length=STRING_LENGTH, null= True),
        'dependencies': list,#(to= string)
    },
    'inputs': list#(to= PropertyDefinition  or PropertyAssignment)
})

InterfaceDefinition = type('InterfaceDefinition', (models.Model,), {
    '__module__': 'tosca',
    'inputs': list#(to= PropertyDefinition or PropertyAssignment)
})

CapabilityDefinition = type('CapabilityDefinition', (models.Model,), {
    '__module__': 'tosca',
    'type': string(max_length=STRING_LENGTH, null= False, default=''),
    'description': description(max_length= DESC_LENGTH, null= True),
    'properties': list,#(to= PropertyDefinition),
    'attributes': list,#(to= AttributeDefinition),
    'valid_source_types': [string],
    'occurrences': range(1,UNBOUNDED),
})

RequirementDefinition = type('RequirementDefinition', (models.Model,), {
    '__module__': 'tosca',
    'capability': string(max_length=STRING_LENGTH, null=False, default=''),
    'node': string(max_length=STRING_LENGTH, null= True),
    'relationship': string(max_length=STRING_LENGTH, null= True) or {
        'type': string(max_length=STRING_LENGTH, null=True),
        'interfaces': list#(to= InterfaceDefinition)
    },
    'occurrences': range(1,UNBOUNDED),
})

#********************************************************************
# Type specific definitions

ArtifactType = type('ArtifactType', (models.Model,), {
    '__module__': 'tosca',
    'derived_from': string(max_length=STRING_LENGTH, null= True),
    'version': Version(),
    'description': description(max_length=DESC_LENGTH, null= True),
    'mime_type': string(max_length=STRING_LENGTH, null= True),
    'file_ext': [string],
    'properties': list#(to= PropertyDefinition)
})

InterfaceType = type('InterfaceType', (models.Model,), {
    '__module__': 'tosca',
    'derived_from': string(max_length=STRING_LENGTH, null= True),
    'version': Version(),
    'description': description(max_length= DESC_LENGTH),
    'inputs': list#(to= PropertyDefinition),
})

DataType = type('DataType', (models.Model,), {
    '__module__': 'tosca',
    'derived_from': string(max_length=STRING_LENGTH, null= True),
    'version': Version(),
    'description': description(max_length=DESC_LENGTH, null=True),
    'constraints': list,#(to= constraint_clause),
    'properties': list#(to= PropertyDefinition),
})

CapabilityType = type('CapabilityType', (models.Model,), {
    '__module__': 'tosca',
    'derived_from': string(max_length=STRING_LENGTH, null= True),
    'version': Version(),
    'description': description(max_length= DESC_LENGTH),
    'properties': list,#(to= PropertyDefinition),
    'attributes': list,#(to=AttributeDefinition),
    'valid_source_type': [string],
})

NodeType = type('NodeType', (models.Model,), {
    '__module__': 'tosca',
    'derived_from': string(max_length=STRING_LENGTH, null=True),
    'version': Version(),
    'description': description(max_length=DESC_LENGTH),
    'properties': list,#(to= PropertyDefinition),
    'attributes': list,#(to=AttributeDefinition),
    'requirements': list,#(to=RequirementDefinition),
    'capabilities': list,#(to= CapabilityDefinition),
    'interfaces': list,#(to= InterfaceDefinition),
    'artifacts' : list#(to= ArtifactDefinition)
})

RelationshipType = type('RelationshipType', (models.Model,), {
    '__module__': 'tosca',
    'derived_from': string(max_length=STRING_LENGTH, null= True),
    'version': Version(),
    'description': description(max_length=DESC_LENGTH),
    'properties': list,#(to= PropertyDefinition),
    'attributes': list,#(to=AttributeDefinition),
    'interfaces': list,#(to= InterfaceDefinition),
    'valid_target_types' : [string]
})

GroupType = type('GroupType', (models.Model,), {
    '__module__': 'tosca',
    'derived_from': string(max_length=STRING_LENGTH, null= True),
    'version': Version(),
    'description': description(max_length=STRING_LENGTH, null=True),
    'properties': list,#(to= PropertyDefinition),
    'members': [string],
    'interfaces': list#(to= InterfaceDefinition)
})

PolicyType = type('PolicyType', (models.Model,), {
    '__module__': 'tosca',
    'derived_from': string(max_length=STRING_LENGTH, null=True),
    'version': Version(),
    'description': description(max_length=DESC_LENGTH),
    'properties': list,#(to= PropertyDefinition),
    'targets': [string]
})

#********************************************************************
# Template specific

CapabilityAssignment = type('CapabilityAssignment', (models.Model,), {
    '__module__': 'tosca',
    'properties': list,#(to=PropertyAssignment),
    'attributes': list#(to=AttributeAssignment)
})

RequirementAssignment = type('RequirementAssignment', (models.Model,), {
    '__module__': 'tosca',
    'capability': string(max_length=STRING_LENGTH, null=True),
    'node': string(max_length=STRING_LENGTH, null= True),
    'relationship': string(max_length=STRING_LENGTH, null= True) or {
        'type': string(max_length=STRING_LENGTH, null= True),
        'properties': list#(to= InterfaceDefinition)
    },
    'node_filter': NodeFilterDefinition
})

NodeTemplate = type('NodeTemplate', (models.Model,), {
    '__module__': 'tosca',
    'type': string(max_length=STRING_LENGTH, null=False, default=''),
    'description': description(max_length= DESC_LENGTH, null= True),
    'directives': [string],
    'properties': list,#(to= PropertyAssignment),
    'attributes': list,#(to= AttributeAssignment),
    'requirements': list,#(to= RequirementAssignment),
    'capabilities': list,#(to= CapabilityAssignment),
    'interfaces': list,#(to= InterfaceDefinition),
    'artifacts': list,#(to= ArtifactDefinition),
    'node_filter': NodeFilterDefinition,
    'copy': string
})

RelationshipTemplate = type('RelationshipTemplate', (models.Model,), {
    '__module__': 'tosca',
    'type': string(max_length=STRING_LENGTH, null= False, default=''),
    'description': description(max_length= DESC_LENGTH, null=True),
    'properties': list,#(to= PropertyAssignment),
    'attributes': list,#(to= AttributeAssignment),
    'interfaces': list,#(to= InterfaceDefinition),
    'copy': string
})

GroupDefinition = type('GroupDefinition', (models.Model,), {
    '__module__': 'tosca',
    'type': string(max_length=STRING_LENGTH, null= False, default=''),
    'description': description(max_length= DESC_LENGTH),
    'properties': list,#(to= PropertyAssignment),
    'members': list,#(to= string),
    'interfaces': list,#(to= InterfaceDefinition)
})

PolicyDefinition = type('PolicyDefinition', (models.Model,), {
    '__module__': 'tosca',
    'type': string(max_length=STRING_LENGTH, null= False, default=''),
    'description': description(max_length=DESC_LENGTH, null=True),
    'properties': list,#(to= PropertyAssignment),
    'targets': [string]
})

TopologyTemplate = type('TopologyTemplate', (models.Model,), {
    '__module__': 'tosca',
    'description': description(max_length=DESC_LENGTH, null=True),
    'inputs': list,#(to= ParameterDefinition),
    'node_templates': list,#(to= NodeTemplate),
    'relationship_templates': list,#(to= RelationshipTemplate),
    'groups': list,#(to= GroupDefinition),
    'policies': list,#(to= PolicyDefinition),
    'outputs': list,#(to= ParameterDefinition),
    'substitution_mappings': string(max_length=STRING_LENGTH, null=True) #NOTE: need to fix this
})

ServiceTemplate = type('ServiceTemplate', (models.Model,), {
    '__module__': 'tosca',
    'tosca_definition_version': string(max_length=STRING_LENGTH, null=True),
    'meta_data': map, #NOTE add keynames
    'description': description(max_length=DESC_LENGTH, null=True),
    'dsl_definitions': string(max_length=STRING_LENGTH, null=True), #NOTE: Need to fix this
    'repositories': list,#(to= RepositoryDefinition),
    'imports': list,#(to= ImportDefinition),
    'artifacts': list,#(to= ArtifactType),
    'data_types': list,#(to= DataType),
    'capability_types': list,#(to= CapabilityType),
    'interface_type': list,#(to= InterfaceType),
    'relationship_types': list,#(to= RelationshipType),
    'node_types': list,#(to= NodeType),
    'group_types': list,#(to= GroupType),
    'policy_types': list,#(to= PolicyType),
    'topology_template': TopologyTemplate()
})

#********************************************************************


