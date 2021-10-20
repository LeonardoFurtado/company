from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        company = self.get_object()
        if company.situation != Company.EXCLUDED:
            company.situation = Company.EXCLUDED
            company.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        if self.action == 'list':
            return Company.objects.exclude(situation='E')
        return super().get_queryset()


class EmployeesViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'username'

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        employee = self.get_object()
        if employee.situation != Employee.EXCLUDED:
            employee.situation = Employee.EXCLUDED
            employee.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        if self.action == 'list':
            return Employee.objects.exclude(situation='E')
        return super().get_queryset()
