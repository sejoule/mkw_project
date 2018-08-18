from django.conf.urls import url, include
from .views import  FileUploadView, ServiceTemplateViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'service_templates', ServiceTemplateViewSet, base_name='service_templates')

urlpatterns = [
    url(r'^', include(router.urls)),
]
