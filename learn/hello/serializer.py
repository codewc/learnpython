#coding=utf8

from rest_framework import serializers

from hello.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        modle = User
        fields = ('id','username','password')
    