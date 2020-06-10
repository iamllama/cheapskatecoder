from django.contrib.auth.models import User
from rest_framework.serializers import  ModelSerializer
from blog.models import *
from rest_framework.serializers import SerializerMethodField, Serializer
from rest_framework import serializers
from django.contrib.auth import authenticate


class BlogModelSerializer(ModelSerializer):
    username = SerializerMethodField()

    def get_username(self, instance):
        return instance.author.username

    class Meta:
        model = Blog
        fields = ('title', 'slug', 'meta_summary', 'blog_content', 'date_published', 'series', 'categories', 'username')
        depth = 1


class SeriesModelSerializer(ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'
        depth = 1


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        depth = 1


# Login Serializer
class LoginSerializer(Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')