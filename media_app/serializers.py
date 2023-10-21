from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User,Group
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','topic', 'message', 'created_on']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password']
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )
