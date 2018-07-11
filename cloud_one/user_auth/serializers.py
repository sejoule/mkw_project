from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('description', 'website',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'groups', 'account',)

class UserAuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name',)