from django.conf.urls import url, include
from .views import UserViewSet, UserAvatarViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'avatar', UserAvatarViewSet, base_name='avatar')

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^avatar/change', AvatarUploadView.as_view()),
]