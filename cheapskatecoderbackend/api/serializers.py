from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.serializers import  ModelSerializer
from blog.models import *
from rest_framework.serializers import SerializerMethodField, Serializer
from rest_framework import serializers
from django.contrib.auth import authenticate


class BlogModelSerializer(ModelSerializer):
    username = SerializerMethodField()
    blog_thumbnail = serializers.SerializerMethodField()
    blog_banner_image = serializers.SerializerMethodField()
    author_profile_photo = serializers.SerializerMethodField()
    author_full_name = serializers.SerializerMethodField()
    date_published = serializers.SerializerMethodField()

    def get_date_published(self, instance):
        return instance.date_published.strftime('%d-%m-%Y - %A')

    def get_author_full_name(self, instance):
        return instance.author.first_name+' '+instance.author.last_name

    def get_author_profile_photo(self, instance):
        try:
            return settings.SITE_URL+instance.author.profile.profile_photo.url
        except Exception as e:
            print(e)
            return ""

    def get_blog_banner_image(self, instance):
        try:
            return settings.SITE_URL+instance.blog_banner_image.url
        except Exception as e:
            return ""

    def get_blog_thumbnail(self, instance):
        try:
            return settings.SITE_URL+instance.blog_thumbnail.url
        except Exception as e:
            return ""

    def get_username(self, instance):
        return instance.author.username

    class Meta:
        model = Blog
        fields = ('title', 'slug', 'meta_summary', 'blog_content', 'date_published', 'series', 'categories', 'username', 'blog_thumbnail',
                'blog_banner_image', 'author_profile_photo', 'author_full_name')
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
