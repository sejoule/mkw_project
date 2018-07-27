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
        fields = ('first_name','last_name','username', 'email', 'account',)

    def create(self, validated_data):
        account_data = validated_data.pop('account')
        user = User.objects.create(**validated_data)
        Account.objects.create(user=user, **account_data)
        return user

    def update(self, instance, validated_data):
        account_data = validated_data.pop('account')
        #if does not exist then handle
        account = instance.account

        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        account.description = account_data.get('description', account.description)
        account.website = account_data.get('website', account.website)
        account.save()

        return instance


class UserAuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name',)