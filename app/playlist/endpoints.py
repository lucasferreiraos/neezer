from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PlaylistViewSet


app_name = 'playlist'

router = DefaultRouter()

router.register(r'playlist', PlaylistViewSet)

urlpatterns = [
    path('', include(router.urls))
]
