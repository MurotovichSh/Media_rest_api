from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','topic', 'message', 'created_on']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password']