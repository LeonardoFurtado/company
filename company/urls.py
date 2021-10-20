from django.contrib import admin
from django.urls import path, include
from api.urls import router as api_router

routes = []
routes.extend(api_router.urls)

urlpatterns = [
    path(r'api/', include((routes, 'company'), namespace='v1')),
    path('admin/', admin.site.urls),
]
