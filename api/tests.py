from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Company, Employee
from model_bakery import baker


class BaseSetup(APITestCase):
    def setUp(self):
        self.company_1 = baker.make('Company')
        self.company_data = {
            "name": "Disney",
            "trading_name": "disney"
        }
        self.company_data_2 = {
            "name": "Netflix",
            "trading_name": "netflix"
        }

        self.employee_1 = baker.make('Employee')
        self.employee_data = {
            "first_name": "Alvo",
            "last_name": "Dumbledore",
            "username": "aldumble",
            "company": [],
        }
        self.employee_data_2 = {
            "first_name": "Severus",
            "last_name": "Snape",
            "username": "lilys2",
            "company": [],
        }

    # Companies
    def create_company(self, data: dict):
        response = self.client.post(
            reverse('v1:company-list'),
            data=data,
        )

        return response

    def get_company(self, company_id: int):
        response = self.client.get(
            reverse('v1:company-detail', args=[int(company_id)]),
        )

        return response

    def delete_company(self, company_id: int):
        response = self.client.delete(
            reverse('v1:company-detail', args=[int(company_id)]),
        )

        return response

    def update_company(self, company_id: int, data: dict):
        response = self.client.put(
            reverse('v1:company-detail', args=[int(company_id)]),
            data=data,
        )

        return response

    def list_companies(self, data: dict = None):
        response = self.client.get(
            reverse('v1:company-list'),
            data=data,
        )

        return response

    def partial_update_company(self, company_id: int, data: dict):
        response = self.client.patch(
            reverse('v1:company-detail', args=[int(company_id)]),
            data=data,
        )

        return response

    # Employees
    def create_employee(self, data: dict):
        response = self.client.post(
            reverse('v1:employee-list'),
            data=data,
        )

        return response

    def get_employee(self, employee_username: str):
        response = self.client.get(
            reverse('v1:employee-detail', args=[str(employee_username)]),
        )

        return response

    def delete_employee(self, employee_username: str):
        response = self.client.delete(
            reverse('v1:employee-detail', args=[str(employee_username)]),
        )

        return response

    def update_employee(self, employee_username: str, data: dict):
        response = self.client.put(
            reverse('v1:employee-detail', args=[str(employee_username)]),
            data=data,
        )

        return response

    def list_employees(self, data: dict = None):
        response = self.client.get(
            reverse('v1:employee-list'),
            data=data,
        )

        return response

    def partial_update_employee(self, employee_username: str, data: dict):
        response = self.client.patch(
            reverse('v1:employee-detail', args=[str(employee_username)]),
            data=data,
        )

        return response


class TestCompany(BaseSetup):
    def test_create_company(self):
        create_company_response = self.create_company(self.company_data)
        self.assertEqual(create_company_response.status_code, status.HTTP_201_CREATED)

        # try to create a company with the same trading_name
        create_company_response = self.create_company(self.company_data)
        self.assertEqual(create_company_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_company_by_id(self):
        retrieve_company_by_id_response = self.get_company(company_id=self.company_1.id)
        self.assertEqual(retrieve_company_by_id_response.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieve_company_by_id_response.json()['name'], self.company_1.name)
        self.assertEqual(retrieve_company_by_id_response.json()['trading_name'], self.company_1.trading_name)

        retrieve_company_by_id_response = self.get_company(company_id=99)
        self.assertEqual(retrieve_company_by_id_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_company(self):
        delete_company_response = self.delete_company(company_id=self.company_1.id)
        self.assertEqual(delete_company_response.status_code, status.HTTP_204_NO_CONTENT)

        get_company_response = self.get_company(self.company_1.id)
        self.assertEqual(get_company_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_company_response.json()['situation'], Company.EXCLUDED)

    def test_update_company(self):
        update_company_response = self.update_company(company_id=self.company_1.id, data=self.company_data_2)
        self.assertEqual(update_company_response.status_code, status.HTTP_200_OK)

    def test_partial_update_company(self):
        partial_update_company_response = self.partial_update_company(
            company_id=self.company_1.id,
            data={"situation": Company.INACTIVE}
        )
        self.assertEqual(partial_update_company_response.status_code, status.HTTP_200_OK)
        get_company_response = self.get_company(self.company_1.id)
        self.assertEqual(get_company_response.json()['situation'], Company.INACTIVE)

    def test_list_companies(self):
        pass


class TestEmployee(BaseSetup):
    def test_create_employee(self):
        create_employee_response = self.create_employee(data=self.employee_data)
        self.assertEqual(create_employee_response.status_code, status.HTTP_201_CREATED)

        create_employee_response = self.create_employee(data=self.employee_data)
        self.assertEqual(create_employee_response.status_code, status.HTTP_400_BAD_REQUEST)
        # TODO: Implement capitalization test

    def test_retrieve_employee(self):
        retrieve_employee_by_id_response = self.get_employee(employee_username=self.employee_1.username)
        self.assertEqual(retrieve_employee_by_id_response.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieve_employee_by_id_response.json()['first_name'], self.employee_1.first_name)
        self.assertEqual(retrieve_employee_by_id_response.json()['last_name'], self.employee_1.last_name)
        self.assertEqual(retrieve_employee_by_id_response.json()['username'], self.employee_1.username)

        retrieve_employee_by_id_response = self.get_employee(employee_username="malfoy")
        self.assertEqual(retrieve_employee_by_id_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_employee(self):
        update_employee_response = self.update_employee(employee_username=self.employee_1.username, data=self.employee_data_2)
        self.assertEqual(update_employee_response.status_code, status.HTTP_200_OK)

    def test_partial_update_employee(self):
        partial_update_employee_response = self.partial_update_employee(
            employee_username=self.employee_1.username,
            data={"situation": Employee.INACTIVE}
        )
        self.assertEqual(partial_update_employee_response.status_code, status.HTTP_200_OK)

        get_employee_response = self.get_employee(employee_username=self.employee_1.username)
        self.assertEqual(get_employee_response.json()['situation'], Employee.INACTIVE)

    def test_delete_employee(self):
        delete_employee_response = self.delete_employee(self.employee_1.username)
        self.assertEqual(delete_employee_response.status_code, status.HTTP_204_NO_CONTENT)

        get_employee_response = self.get_employee(employee_username=self.employee_1.username)
        self.assertEqual(get_employee_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_employee_response.json()['situation'], Employee.EXCLUDED)

    def test_list_emplyees(self):
        pass
