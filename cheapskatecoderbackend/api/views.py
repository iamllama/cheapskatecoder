from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.permissions import AllowAny, AllowAny
from api.serializers import *
from blog.models import *
from knox.models import AuthToken
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogModelViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Blog.objects.filter(is_published=True).order_by('-id')
    serializer_class = BlogModelSerializer

    def retrieve(self, request, pk):
        if pk is not None:
            specific_blog_instance = Blog.objects.filter(slug=pk).first()
            serialized_data = BlogModelSerializer(specific_blog_instance)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SeriesModelViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Series.objects.all()
    serializer_class = SeriesModelSerializer



class CategoryModelViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

class LoginAPI(APIView):
    serializer_class = LoginSerializer
    queryset = User.objects.none()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        user = serializer.validated_data
        user_data = UserModelSerializer(user, many=False)
        user_data_and_token = {'token': AuthToken.objects.create(user)[1]}
        user_data_and_token.update(user_data.data)
        if user:
                return Response(user_data_and_token)
        else:
                return Response({"Error": "User credentials are invalid!"}, status=status.HTTP_400_BAD_REQUEST)

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny, ]


class UserDetails(ModelViewSet):
    queryset = User.objects.none()
    serializer_class = UserModelSerializer
    permission_classes = (AllowAny, )
    http_method_names = ('head', 'option', 'get')

    def list(self, request):
        queryset = User.objects.get(username=request.user)
        serializer = self.serializer_class(queryset)

        return Response(serializer.data)


class TopNineBlogs(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        top_nine_blogs = Blog.objects.all().order_by('-id')[:9]
        serialized_data = BlogModelSerializer(top_nine_blogs, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
