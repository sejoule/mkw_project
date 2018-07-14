from django.conf.urls import url, include
from .views import  Attribute

urlpatterns = [
    #---------Example urls-----------
    url(r'attribute/create$', Attribute.as_view()), #HTTP Method=POST
    url(r'attribute/delete$', Attribute.as_view()), #example urls HTTP Method = DELETE
    url(r'attribute/update$', Attribute.as_view()), #HTTP Method = PUT
    url(r'attribute/([a-zA-Z0-9_.-]+)/$',Attribute.as_view()), #HTTP Method = GET
    #---------------------------------
]
