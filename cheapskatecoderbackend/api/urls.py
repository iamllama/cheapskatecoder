from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from api import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



router = DefaultRouter()

router.register('blog', views.BlogModelViewSet, basename='blog')
router.register('category', views.CategoryModelViewSet, basename='category')
router.register('series', views.SeriesModelViewSet, basename='series')
router.register('user', views.UserModelViewSet, basename='user')
router.register('user-details', views.UserDetails, basename='user-details')


urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('login', views.LoginAPI.as_view(), name='login'),
   path('top-9-blogs', views.TopNineBlogs.as_view(), name='top-9'),
]

urlpatterns += router.urls
