from django.conf.urls import url, include
from .views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'list$',UserList.as_view()),
    # url(r'create$', UserView.as_view()), #HTTP Method=POST
    # url(r'delete$', UserView.as_view()), #example urls HTTP Method = DELETE
    # url(r'update/([a-zA-Z0-9_.-]+)$', UserView.as_view()), #HTTP Method = PUT
    # url(r'([a-zA-Z0-9_.-]+)$',UserView.as_view()), #HTTP Method = GET
]