from django.contrib import admin
from django.urls import path, include
from api.urls import router as api_router
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Company API",
      default_version='v1',
      description="A API that allow to do basic crud methods on Company and Employee models.",
      contact=openapi.Contact(email="srleonardofurtado@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

routes = []
routes.extend(api_router.urls)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include((routes, 'company'), namespace='v1')),
    path('admin/', admin.site.urls),
]
