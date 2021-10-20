from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Company, Employee


class EmployeeSerializer(ModelSerializer):
    company = serializers.SlugRelatedField(
        many=True, queryset=Company.objects.all(), slug_field="name"
    )

    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name", "username", "company", "situation"]
        lookup_field = "username"
        extra_kwargs = {
            "url": {"lookup_field": "username"},
        }

    def validate_username(self, value):
        value = value.replace(" ", "").lower()

        if self.instance:
            instance_id = self.instance.id
        else:
            instance_id = None

        try:
            Employee.objects.exclude(id=instance_id).get(username=value)
        except ObjectDoesNotExist:
            pass
        else:
            raise serializers.ValidationError({"username": "This username already exists"}, code="invalid")

        return value


class CompanySerializer(ModelSerializer):
    employee = serializers.SerializerMethodField("get_employees_names")

    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "trading_name",
            "employee",
            "updated",
            "created",
            "situation",
        ]

    @staticmethod
    def get_employees_names(obj):
        employees_names_list = [employee.username for employee in obj.employee.all()]

        return employees_names_list

    def validate_name(self, value):
        value = value.lower()

        if self.instance:
            instance_id = self.instance.id
        else:
            instance_id = None

        try:
            Company.objects.exclude(id=instance_id).get(name=value)
        except ObjectDoesNotExist:
            pass
        else:
            raise serializers.ValidationError({"name": "This name already exists"}, code="invalid")

        return value
