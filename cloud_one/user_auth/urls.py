from django.conf.urls import url, include
from .views import users_list, user_specific

urlpatterns = [
    url(r'^$', users_list),
    url(r'^([0-9]+)/$',user_specific),
]