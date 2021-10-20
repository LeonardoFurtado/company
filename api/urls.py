from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'employees', views.EmployeesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]