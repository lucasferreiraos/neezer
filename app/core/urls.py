from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Neezer API',
        default_version='v1',
        description='Simple API to manage favorite songs',
        contact=openapi.Contact(email='lucasferreiraek@gmail.com'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.endpoints', namespace='authentication')),
    path('artist/', include('artist.endpoints', namespace='artist')),
    path('playlist/', include('playlist.endpoints', namespace='playlist')),
    re_path(
        r'swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    )
]
