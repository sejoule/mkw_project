from mongoengine import *

STRING_LENGTH = 100
DESC_LENGTH   = 300
UNBOUND       = 10000000

class Any(IntField or StringField or BooleanField):
    pass

class Scalar(IntField, StringField, BooleanField):
    pass

class RegExpression(StringField):
    pass

class Value(IntField, StringField,BooleanField):
    pass

class PropertyValueExpression(StringField):
    pass

class AttributeValueExpression(StringField):
    pass

#*****Operators******
# equal              = '='
# greater_than       = 'gt'
# greater_or_equal   = 'gte'
# less_than          = 'lt'
# less_or_equal      = 'lte'
# in_range           = 'in'
# # valid_values     = '???'
# # length           = 'size'.
# # min_length       = 'size__gte'
# # max_length       = 'size__lte'
# # pattern          = '???'
#
# ******************* Reference*************

# ne – not equal to
# lt – less than
# lte – less than or equal to
# gt – greater than
# gte – greater than or equal to
# not – negate a standard check, may be used before other operators (e.g. Q(age__not__mod=5))
# in – value is in list (a list of values should be provided)
# nin – value is not in list (a list of values should be provided)
# mod – value % x == y, where x and y are two provided values
# all – every item in list of values provided is in array
# size – the size of the array is
# exists – value for field exists


class Version(Document):
    major_version = IntField(default=0, null= False)
    minor_version = IntField(default=0, null=False)
    fixed_version= IntField(null=True)
    qualifier= StringField(null=True, max_length=STRING_LENGTH)
    build_version= IntField(null=True)


class Credential(Document):
    protocol   = StringField(null=True, max_length=STRING_LENGTH)
    token_type = StringField(null=False, max_length=STRING_LENGTH, default='password')
    token      = StringField(null=False, max_length=STRING_LENGTH)
    keys       = MapField(StringField(max_length=STRING_LENGTH), null=True)
    userh       = StringField(null=True, max_length=STRING_LENGTH)

class ConstraintClause(Document):
    operator = StringField(null=True, max_length=STRING_LENGTH)
    operands = Any or Scalar or RegExpression


class State(Document):
    value        = StringField(null=False, max_length=STRING_LENGTH),
    transitional = BooleanField(default=True)

class Range(Document):
    lower_bound = IntField(default=1, null= False)
    upper_bound =  IntField(default= UNBOUND, null=False)


class PropertyFilterDefinition(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    property_name = StringField(null=True, max_length=STRING_LENGTH)
    property_constraint_clause = ConstraintClause()


class NodeFilterDefinition(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    properties = ListField(PropertyFilterDefinition),
    capabilities =ListField(StringField(null=True, max_length=STRING_LENGTH)) #NOTE these are capability names or capability type names


class RepositoryDefinition(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    description = StringField(null=False, max_length=DESC_LENGTH)
    url = URLField()
    credential = Credential(),


class ArtifactDefinition(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type = StringField(null=True, max_length=STRING_LENGTH)
    file = StringField(null=True, max_length=STRING_LENGTH)
    repository =StringField(null=True, max_length=STRING_LENGTH)
    description = StringField(null=False, max_length=DESC_LENGTH),
    deploy_path = StringField(null=True, max_length=STRING_LENGTH)


class ImportDefinition(Document): 
    file = StringField(null=True, max_length=STRING_LENGTH)
    repository =StringField(null=True, max_length=STRING_LENGTH)
    namespace_uri = StringField(null=True, max_length=STRING_LENGTH)
    namespace_prefix = StringField(null=True, max_length=STRING_LENGTH)


class PropertyDefinition(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type = StringField(null=True, max_length=STRING_LENGTH)
    description = StringField(null=False, max_length=DESC_LENGTH),
    required = BooleanField(default = True),
    default = Any(),
    status = StringField(null=True, max_length=STRING_LENGTH)
    constraints = ListField(ConstraintClause)
    entry_schema = StringField(null=True, max_length=STRING_LENGTH)


class AttributeDefinition(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type = StringField(null=True, max_length=STRING_LENGTH)
    description = StringField(null=False, max_length=DESC_LENGTH),
    default = Any(),
    status = StringField(null=True, max_length=STRING_LENGTH)
    entry_schema = StringField(null=True, max_length=STRING_LENGTH)


class PropertyAssignment(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    value = Value() or PropertyValueExpression()


class AttributeAssignment(Document):
    name = StringField(null=False, max_length=STRING_LENGTH)
    value = Value() or AttributeValueExpression()
    concrete_model = Document

class ParameterDefinition(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type = StringField(null=True, max_length=STRING_LENGTH)
    value = Any()


class OperationDefinition(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    description = StringField(null=False, max_length=DESC_LENGTH),
    implementation = StringField(null=False, max_length=DESC_LENGTH) \
    or {
        'primary': StringField(null=True, max_length=STRING_LENGTH),
        'dependencies': ListField(StringField(null=True, max_length=STRING_LENGTH))
        }
    inputs = ListField(PropertyDefinition() or PropertyAssignment())


class InterfaceDefinition(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type = StringField(null=True, max_length=STRING_LENGTH)
    inputs = ListField(PropertyDefinition() or PropertyAssignment())


class CapabilityDefinition(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type = StringField(null=True, max_length=STRING_LENGTH)
    description = StringField(null=False, max_length=DESC_LENGTH)
    properties = ListField(PropertyDefinition())
    attributes = ListField(AttributeDefinition())
    valid_source_types = ListField(StringField(null=True, max_length=STRING_LENGTH))
    occurrences = Range()


class RequirementDefinition(Document): 
    capability = StringField(null=True, max_length=STRING_LENGTH)
    node = StringField(null=True, max_length=STRING_LENGTH)
    relationship = StringField(null=True, max_length=STRING_LENGTH) \
    or {
        'type': StringField(null=True, max_length=STRING_LENGTH),
        'interfaces': ListField(InterfaceDefinition())
        }
    occurrences = Range(),

class ArtifactType(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    derived_from = StringField(null=True, max_length=STRING_LENGTH)
    version = Version(),
    description = StringField(null=True, max_length=DESC_LENGTH)
    mime_type = StringField(null=True, max_length=STRING_LENGTH)
    file_ext = [StringField(null=True, max_length=STRING_LENGTH)]
    properties = ListField(PropertyDefinition())

class InterfaceType(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    derived_from = StringField(null=True, max_length=STRING_LENGTH)
    version = Version(),
    description = StringField(null=True, max_length=DESC_LENGTH)
    inputs = ListField(PropertyDefinition())


class DataType(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    # type           = StringField(null=False, max_length=STRING_LENGTH)
    derived_from   = StringField(null=False, max_length=STRING_LENGTH)
    version        = Version()
    description    = StringField(null=False, max_length=DESC_LENGTH)
    constraints    = ListField(ConstraintClause()),#(to= constraint_clause),
    properties     = ListField(PropertyDefinition())#(to= PropertyDefinition),

class CapabilityType(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    # type = StringField(null=False, max_length=STRING_LENGTH)
    derived_from =  StringField(null=False, max_length=STRING_LENGTH)
    version =  Version()
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(PropertyDefinition())
    attributes =  ListField(AttributeDefinition())
    valid_source_type =  [StringField(null=False, max_length=STRING_LENGTH)]


class NodeType(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    derived_from =  StringField(null=False, max_length=STRING_LENGTH)
    version = Version()
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(PropertyDefinition())
    attributes =  ListField(AttributeDefinition())
    requirements =  ListField(RequirementDefinition())
    capabilities =  ListField(CapabilityDefinition())
    interfaces =  ListField(InterfaceDefinition())
    artifacts = ListField(ArtifactDefinition())


class RelationshipType(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    derived_from =  StringField(null=False, max_length=STRING_LENGTH)
    version = Version()
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(PropertyDefinition())
    attributes =  ListField(AttributeDefinition())
    interfaces =  ListField(InterfaceDefinition())
    valid_target_types = [StringField(null=False, max_length=STRING_LENGTH)]


class GroupType(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    derived_from =  StringField(null=False, max_length=STRING_LENGTH)
    version = Version()
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(PropertyDefinition())
    members =  [StringField(null=False, max_length=STRING_LENGTH)]
    interfaces =  ListField(InterfaceDefinition())


class PolicyType(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    derived_from =  StringField(null=False, max_length=STRING_LENGTH)
    version = Version()
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(PropertyDefinition())
    targets =  [StringField(null=False, max_length=STRING_LENGTH)]

#********************Template Specifications**************************************

class CapabilityAssignment(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    properties =  ListField(PropertyAssignment())
    attributes =  ListField(AttributeAssignment())


class RequirementAssignment(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    capability =  StringField(null=False, max_length=STRING_LENGTH)
    node =  StringField(null=False, max_length=STRING_LENGTH)
    relationship =  StringField(null=False, max_length=STRING_LENGTH) \
    or {
        'type':  StringField(null=False, max_length=STRING_LENGTH),
        'properties':  ListField(InterfaceDefinition())
    }
    node_filter =  NodeFilterDefinition()


class NodeTemplate(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type =  StringField(null=False, max_length=STRING_LENGTH)
    description =  StringField(null=False, max_length=DESC_LENGTH)
    directives =  [StringField(null=False, max_length=STRING_LENGTH)],
    properties =  ListField(PropertyAssignment())
    attributes =  ListField(AttributeAssignment())
    requirements =  ListField(RequirementAssignment())
    capabilities =  ListField(CapabilityAssignment())
    interfaces =  ListField(InterfaceDefinition())
    artifacts =  ListField(ArtifactDefinition())
    node_filter =  NodeFilterDefinition()
    copy =  StringField(null=False, max_length=STRING_LENGTH)


class RelationshipTemplate(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type =  StringField(null=False, max_length=STRING_LENGTH)
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(PropertyAssignment)
    attributes =  ListField(AttributeAssignment)
    interfaces =  ListField(InterfaceDefinition)
    copy =  StringField(null=False, max_length=STRING_LENGTH)


class GroupDefinition(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type =  StringField(null=False, max_length=STRING_LENGTH)
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(PropertyAssignment())
    members =  ListField(StringField(null=False, max_length=STRING_LENGTH)),
    interfaces =  ListField(InterfaceDefinition())


class PolicyDefinition(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type =  StringField(null=False, max_length=STRING_LENGTH)
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(PropertyAssignment())
    targets =  [StringField(null=False, max_length=STRING_LENGTH)]


class TopologyTemplate(Document):
    description =  StringField(null=False, max_length=DESC_LENGTH)
    inputs =  ListField(PropertyDefinition)
    node_templates =  ListField(NodeTemplate())
    relationship_templates =  ListField(RelationshipTemplate())
    groups =  ListField(GroupDefinition())
    policies =  ListField(PolicyDefinition())
    outputs =  ListField(ParameterDefinition())
    substitution_mappings =  StringField(null=False, max_length=STRING_LENGTH) #NOTE: need to fix this


class ServiceTemplate(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    tosca_definition_version =  Version()
    meta_data =  (StringField(null=False, max_length=STRING_LENGTH)), #NOTE add keynames
    description = StringField(null=False, max_length=DESC_LENGTH)
    dsl_definitions =  StringField(null=False, max_length=STRING_LENGTH) #NOTE: Need to fix this
    repositories =  ListField(RepositoryDefinition())
    imports =  ListField(ImportDefinition())
    artifacts =  ListField(ArtifactDefinition())
    data_types =  ListField(DataType())
    capability_types =  ListField(CapabilityType())
    interface_types =  ListField(InterfaceType())
    relationship_types =  ListField(RelationshipType())
    node_types =  ListField(NodeType())
    group_types =  ListField(GroupType())
    policy_types =  ListField(PolicyType())
    topology_template =  TopologyTemplate()
