from rest_framework.viewsets import ModelViewSet
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from api.serializers import *
from blog.models import *


class BlogModelViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer


class SeriesModelViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Series.objects.all()
    serializer_class = SeriesModelSerializer



class CategoryModelViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
