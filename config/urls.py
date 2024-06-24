from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Pinterest Api",
        default_version='v1',
        description="API Documentation"),
    public=True,
    permission_classes=[AllowAny, ],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    # apps urls
    path('api/v1/', include('pin.urls')),
    path('api/v1/contact/', include('base.urls')),
    path('api/v1/auth/', include('authorization.urls')),
    # swagger urls
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # media and static urls
    re_path(r'^static/(?P<path>.*)$', serve),
    re_path(
        r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
