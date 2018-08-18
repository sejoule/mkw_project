# from django.test import TestCase
# from rest_framework_yaml.parsers import YAMLParser
# from rest_framework_yaml.renderers import YAMLRenderer
#
# # Create your tests here.
#
#
# def test_parse(data):
#     parser = YAMLParser()
#     results = parser.parse(data)
#     return results
#
# if __name__ == "__main__":
#     res = test_parse(
# "node_types:"+
# "  WP_loadbalancer:"+
# "    derived_from: tosca.nodes.LoadBalancer"+
# "    requirements:"+
# "        - webapplication:"+
# "            capability: tosca.capabilities.Endpoint"+
# "            relationship: tosca.relationships.RoutesTo"+
# "            node: tosca.nodes.WebApplication"
#     )
#
#     print(res)