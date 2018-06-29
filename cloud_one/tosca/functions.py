from django.db import models
from metamodels import list, string, integer

#************************************************************
# functions

def concat(strings = list(to=string)):
    result = ''
    for string in strings:
        result += string
    return result

def token(string_with_tokens, string_of_token_chars, substring_index):
    pass


#************************************************************
# property functions

def get_input(input_name):
    #query the db and return the value of the property
    #need the Id's of objects within the template
    pass

def get_property(model_name, req_cap_name, property_name, nested_prop):
    #query the db for the property item and use
    #need the id's of the objects.
    pass

def get_attribute(model_name, req_cap_name, attribute_name, nested_attr):
    #query the db for the property item and use
    #need the id's of the objects.
    pass

def get_operation(model_name, req_cap_name, operation_name, output_var_name):
    #query the db for the property item and use
    #need the id's of the objects.
    pass

#************************************************************
# navigation functions

def get_nodes_of_type(node_type_name):
    #query the db and find the nodes of the type
    #relateed to this service template
    #return the Node TARGETS
    pass

#************************************************************
# artifact functions

def get_artifact(model_name, artifact_name, location, remove):
    #query the db for the property item and use
    #need the id's of the objects.
    pass



