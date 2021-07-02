from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ArtistViewSet, TrackViewSet

app_name = 'artist'

router = DefaultRouter()
router.register(r'artist', ArtistViewSet)
router.register(r'track', TrackViewSet)

urlpatterns = [
    path('', include(router.urls))
]
