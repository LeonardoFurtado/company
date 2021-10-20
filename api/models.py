from django.db import models


class Company(models.Model):
    """Model used to represent a Company

    Attributes:
        name: unique company name.
        trading_name: not unique name, also called `nome fantasia`.
        situation: describe if company is active, inactive or excluded.
        updated: last update.
        created: creation date.
    """
    ACTIVE = 'A'
    INACTIVE = 'I'
    EXCLUDED = 'E'
    SITUATION_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (EXCLUDED, 'Excluded'),
    ]
    trading_name = models.CharField(max_length=150, verbose_name='Trading name')
    name = models.CharField(max_length=150, unique=True, verbose_name='Name', blank=False, null=False)
    situation = models.CharField(max_length=1, choices=SITUATION_CHOICES, default=ACTIVE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Model used to represent a Employee

    Attirbutes:
        first_name: employee first name
        last_name: employee last name
        username: unique username of an employee
        company: companies to which this employee belongs
        situation: describe if company is active, inactive or excluded.
        updated: last update.
        created: creation date.
    """
    ACTIVE = 'A'
    INACTIVE = 'I'
    EXCLUDED = 'E'
    SITUATION_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (EXCLUDED, 'Excluded'),
    ]
    first_name = models.CharField(max_length=150, verbose_name='First name')
    last_name = models.CharField(max_length=150, verbose_name='Last name')
    username = models.CharField(max_length=150, unique=True, verbose_name='Username', blank=False, null=False)
    company = models.ManyToManyField(Company, related_name='employee')
    situation = models.CharField(max_length=1, choices=SITUATION_CHOICES, default=ACTIVE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
