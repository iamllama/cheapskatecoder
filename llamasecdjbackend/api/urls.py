from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()

router.register('blog', views.BlogModelViewSet, basename='blog')
router.register('category', views.CategoryModelViewSet, basename='category')
router.register('series', views.SeriesModelViewSet, basename='series')


urlpatterns = [

]

urlpatterns += router.urls