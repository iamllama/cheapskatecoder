from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from api.serializers import *
from blog.models import *
from knox.models import AuthToken


class BlogModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Blog.objects.filter(is_published=True)
    serializer_class = BlogModelSerializer


class SeriesModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Series.objects.all()
    serializer_class = SeriesModelSerializer



class CategoryModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
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
    permission_classes = [IsAuthenticated, ]


class UserDetails(ModelViewSet):
    queryset = User.objects.none()
    serializer_class = UserModelSerializer
    permission_classes = (IsAuthenticated, )
    http_method_names = ('head', 'option', 'get')

    def list(self, request):
        queryset = User.objects.get(username=request.user)
        serializer = self.serializer_class(queryset)
        print(serializer.data)

        return Response(serializer.data)
