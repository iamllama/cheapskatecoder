from blog.models import *
from rest_framework.serializers import  ModelSerializer


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
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
