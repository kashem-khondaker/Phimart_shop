from django.contrib import admin
from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import api_root_view

schema_view = get_schema_view(
   openapi.Info(
      title="PhiMart E-commerce API",
      default_version='v1',
      description="API doc details",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kashem.khondaker@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root_view),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/' , include('api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
] + debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)