from django.contrib.auth.models import User
from rest_framework.serializers import  ModelSerializer
from blog.models import *
from rest_framework.serializers import SerializerMethodField


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