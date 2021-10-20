from django.db import models


class Company(models.Model):
    """Model used to represent a Company

    Attributes:
        name: Company name
        trading_name:
        situation:
        updated:
        created:
    """
    ACTIVE = 'A'
    INACTIVE = 'I'
    EXCLUDED = 'E'
    SITUATION_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (EXCLUDED, 'Excluded'),
    ]
    trading_name = models.CharField(max_length=150, verbose_name='Name')
    name = models.CharField(max_length=150, unique=True, verbose_name='Trading name', blank=False, null=False)
    situation = models.CharField(max_length=1, choices=SITUATION_CHOICES, default=ACTIVE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trading_name


class Employee(models.Model):
    """
    first_name:
    last_name:
    username:
    company:
    situation:
    updated:
    created:
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
