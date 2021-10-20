from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Company, Employee


class EmployeeSerializer(ModelSerializer):
    company = serializers.SlugRelatedField(
        many=True,
        queryset=Company.objects.all(),
        slug_field='trading_name'
    )

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'username', 'company', 'situation']
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }


class CompanySerializer(ModelSerializer):
    employee = serializers.SerializerMethodField('get_employees_names')

    class Meta:
        model = Company
        fields = ['id', 'name', 'trading_name', 'employee', 'updated', 'created', 'situation']

    @staticmethod
    def get_employees_names(obj):
        employees_names_list = [employee.username for employee in obj.employee.all()]

        return employees_names_list
