from mongoengine import *
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
import yaml

STRING_LENGTH = 100
DESC_LENGTH   = 300
UNBOUND       = 10000000

class Any(IntField or StringField or BooleanField):
    pass

class Scalar(IntField, StringField, BooleanField):
    pass

class RegExpression(StringField):
    pass

class Value(IntField, StringField, BooleanField):
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


class Version(EmbeddedDocument):
    major_version = IntField(default=0, null= False)
    minor_version = IntField(default=0, null=False)
    fixed_version= IntField(null=True)
    qualifier= StringField(null=True, max_length=STRING_LENGTH)
    build_version= IntField(null=True)

    def clean(self):
        if self.major_version is None or -1:
            raise ValidationError('major version is required')
        if self.minor_version is None or -1:
            raise ValidationError('minor version is required')
        if self.fixed_version is None or -1:
            raise ValidationError('Major version is required')

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


class NodeFilterDefinition(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    properties = ListField(PropertyFilterDefinition),
    capabilities =ListField(StringField(null=True, max_length=STRING_LENGTH)) #NOTE these are capability names or capability type names


class RepositoryDefinition(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    description = StringField(null=False, max_length=DESC_LENGTH)
    url = URLField()
    credential = Credential(),


class ArtifactDefinition(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type = StringField(null=True, max_length=STRING_LENGTH)
    file = StringField(null=True, max_length=STRING_LENGTH)
    repository =StringField(null=True, max_length=STRING_LENGTH)
    description = StringField(null=False, max_length=DESC_LENGTH),
    deploy_path = StringField(null=True, max_length=STRING_LENGTH)


class ImportDefinition(EmbeddedDocument):
    file = StringField(null=True, max_length=STRING_LENGTH)
    repository =StringField(null=True, max_length=STRING_LENGTH)
    namespace_uri = StringField(null=True, max_length=STRING_LENGTH)
    namespace_prefix = StringField(null=True, max_length=STRING_LENGTH)


class PropertyDefinition(EmbeddedDocument):
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


class PropertyAssignment(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    value = Value() or PropertyValueExpression()

    def clean(self):
        if self.name is None:
            raise ValidationError('Property Assignment requires a name')
        if self.value is None:
            raise ValidationError('Property Assignment requires a value')


class AttributeAssignment(EmbeddedDocument):
    name = StringField(null=False, max_length=STRING_LENGTH)
    value = Value() or AttributeValueExpression()
    # concrete_model = Document NOTE: review this

class ParameterDefinition(EmbeddedDocument):
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


class InterfaceDefinition(EmbeddedDocument):
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

class InterfaceType(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    derived_from = StringField(null=True, max_length=STRING_LENGTH)
    version = Version(),
    description = StringField(null=True, max_length=DESC_LENGTH)
    inputs = ListField(PropertyDefinition())


class DataType(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    # type           = StringField(null=False, max_length=STRING_LENGTH)
    derived_from   = StringField(null=False, max_length=STRING_LENGTH)
    version        = Version()
    description    = StringField(null=False, max_length=DESC_LENGTH)
    constraints    = ListField(ConstraintClause()),#(to= constraint_clause),
    properties     = ListField(PropertyDefinition())#(to= PropertyDefinition),

class CapabilityType(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    # type = StringField(null=False, max_length=STRING_LENGTH)
    derived_from =  StringField(null=False, max_length=STRING_LENGTH)
    version =  Version()
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(PropertyDefinition())
    attributes =  ListField(AttributeDefinition())
    valid_source_type =  [StringField(null=False, max_length=STRING_LENGTH)]


class NodeType(EmbeddedDocument):
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


class RelationshipType(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    derived_from =  StringField(null=False, max_length=STRING_LENGTH)
    version = Version()
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(PropertyDefinition())
    attributes =  ListField(AttributeDefinition())
    interfaces =  ListField(InterfaceDefinition())
    valid_target_types = [StringField(null=False, max_length=STRING_LENGTH)]


class GroupType(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    derived_from =  StringField(null=False, max_length=STRING_LENGTH)
    version = Version()
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(PropertyDefinition())
    members =  [StringField(null=False, max_length=STRING_LENGTH)]
    interfaces =  ListField(InterfaceDefinition())


class PolicyType(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    derived_from =  StringField(null=False, max_length=STRING_LENGTH)
    version = Version()
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(PropertyDefinition())
    targets =  [StringField(null=False, max_length=STRING_LENGTH)]

#********************Template Specifications**************************************

class CapabilityAssignment(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    properties =  ListField(PropertyAssignment())
    attributes =  ListField(AttributeAssignment())


class RequirementAssignment(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    capability =  StringField(null=False, max_length=STRING_LENGTH)
    node =  StringField(null=False, max_length=STRING_LENGTH)
    relationship =  StringField(null=False, max_length=STRING_LENGTH) \
    or {
        'type':  StringField(null=False, max_length=STRING_LENGTH),
        'properties':  ListField(InterfaceDefinition())
    }
    node_filter =  NodeFilterDefinition()

    def clean(self):
        if self.name is None:
            raise ValidationError('Requirement Assignemnt requires a name')


class NodeTemplate(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type =  StringField(null=False, max_length=STRING_LENGTH)
    description =  StringField(null=False, max_length=DESC_LENGTH)
    directives =  [StringField(null=False, max_length=STRING_LENGTH)], #TODO change this to a list
    properties =  ListField(EmbeddedDocumentField(PropertyAssignment))
    attributes =  ListField(EmbeddedDocumentField(AttributeAssignment))
    requirements =  ListField(EmbeddedDocumentField(RequirementAssignment))
    capabilities =  ListField(EmbeddedDocumentField(CapabilityAssignment))
    interfaces =  ListField(EmbeddedDocumentField(InterfaceDefinition))
    artifacts =  ListField(EmbeddedDocumentField(ArtifactDefinition))
    node_filter =  EmbeddedDocumentField(NodeFilterDefinition)
    copy =  StringField(null=False, max_length=STRING_LENGTH)

    def clean(self):
        if self.name is None:
            raise ValidationError('Node template requires a name')
        if self.type is None:
            raise ValidationError('Node template requires a type')


class RelationshipTemplate(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type =  StringField(null=False, max_length=STRING_LENGTH)
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(EmbeddedDocumentField(PropertyAssignment))
    attributes =  ListField(EmbeddedDocumentField(AttributeAssignment))
    interfaces =  ListField(EmbeddedDocumentField(InterfaceDefinition))
    copy =  StringField(null=False, max_length=STRING_LENGTH)

    def clean(self):
        if self.name is None:
            raise ValidationError('Relationship template requires a name')
        if self.type is None:
            raise ValidationError('Relationship template requires a type')


class GroupDefinition(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type =  StringField(null=False, max_length=STRING_LENGTH)
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(EmbeddedDocumentField(PropertyAssignment))
    members =  ListField(StringField(null=False, max_length=STRING_LENGTH)),
    interfaces =  ListField(EmbeddedDocumentField(InterfaceDefinition))


class PolicyDefinition(EmbeddedDocument):
    name = StringField(null=True, max_length=STRING_LENGTH)
    type =  StringField(null=False, max_length=STRING_LENGTH)
    description =  StringField(null=False, max_length=DESC_LENGTH)
    properties =  ListField(EmbeddedDocumentField(PropertyAssignment))
    targets =  [StringField(null=False, max_length=STRING_LENGTH)]


class TopologyTemplate(EmbeddedDocument):
    description =  StringField(null=False, max_length=DESC_LENGTH)
    inputs =  ListField(EmbeddedDocumentField(PropertyDefinition))
    node_templates =  ListField(EmbeddedDocumentField(NodeTemplate))
    relationship_templates =  ListField(EmbeddedDocumentField(RelationshipTemplate))
    groups =  ListField(EmbeddedDocumentField(GroupDefinition))
    policies =  ListField(EmbeddedDocumentField(PolicyDefinition))
    outputs =  ListField(EmbeddedDocumentField(ParameterDefinition))
    substitution_mappings =  StringField(null=False, max_length=STRING_LENGTH) #NOTE: need to fix this

    def clean(self):
        if self.node_templates is []:
            raise ValidationError('None Templates are required')
        for node_template in self.node_templates:
            node_template.clean()

class ServiceTemplate(Document):
    name = StringField(null=True, max_length=STRING_LENGTH)
    tosca_definition_version =  EmbeddedDocumentField(Version)
    meta_data =  (StringField(null=False, max_length=STRING_LENGTH)), #NOTE add keynames
    description = StringField(null=False, max_length=DESC_LENGTH)
    dsl_definitions =  StringField(null=False, max_length=STRING_LENGTH) #NOTE: Need to fix this
    repositories =  ListField(EmbeddedDocumentField(RepositoryDefinition))
    imports =  ListField(EmbeddedDocumentField(ImportDefinition))
    artifacts =  ListField(EmbeddedDocumentField(ArtifactDefinition))
    data_types =  ListField(EmbeddedDocumentField(DataType))
    capability_types =  ListField(EmbeddedDocumentField(CapabilityType))
    interface_types =  ListField(EmbeddedDocumentField(InterfaceType))
    relationship_types =  ListField(EmbeddedDocumentField(RelationshipType))
    node_types =  ListField(EmbeddedDocumentField(NodeType))
    group_types =  ListField(EmbeddedDocumentField(GroupType))
    policy_types =  ListField(EmbeddedDocumentField(PolicyType))
    topology_template =  EmbeddedDocumentField(TopologyTemplate)

    def clean(self):
        if self.name is None:
            raise ValidationError('name is a required field')
        if self.topology_template is None:
            raise ValidationError('Service Template should have a topology_template')
        self.topology_template.clean()


# *****************************************************************************************
# This is used to represent the service template file that has been uploaded. This data is
# stored in the Relational database instead of NoSQL.
# *****************************************************************************************

class ServiceTemplateFile(models.Model):
    file = models.FileField(blank=True, null=True)
    template_name = models.CharField(max_length=60, null= True)
    template_id = models.CharField(max_length=60, null=True) #NOTE: reference to the service template _id
    user = models.ForeignKey(User, on_delete=CASCADE, null= True) #NOTE the user that uploaded the template
    created_date = models.DateTimeField(null=True)
