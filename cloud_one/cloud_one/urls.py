"""cloud_one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from user_auth.views import UserLogoutAllView
# from user_auth.serializers import UserSerializer
from django.contrib.auth.models import User



# router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #*********Top level urls***********
    url(r'^', include('user_auth.urls')),
    url(r'^tosca/', include('tosca.urls')),

    #NOTE: admin and auth urls
    url(r'^admin', admin.site.urls),
    url(r'^api-user_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-user_auth/logout', UserLogoutAllView.as_view(), name='user-logout-all'),
    url(r'^api-token-user_auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token), # we may not need this

]

