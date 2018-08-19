from django.db import models
from tosca.models import ServiceTemplateFile
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL


# Create your models here.

AppState = {
    'CREATED'    :0,
    'RUNNING'    :1,
    'PAUSED'     :2,
    'TERMINATED' :3
}

class Application(models.Model):
    name = models.CharField(max_length=60)
    template_file = models.ForeignKey(ServiceTemplateFile, null=True, on_delete=SET_NULL)
    state = models.IntegerField(default=AppState['CREATED'])