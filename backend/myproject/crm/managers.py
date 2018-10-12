from django.db import models


class PersonManager(models.Manager):

    def get_queryset(self):
        return super(PersonManager, self).get_queryset().filter(person_type='u')


class CompanyManager(models.Manager):

    def get_queryset(self):
        return super(CompanyManager, self).get_queryset().filter(company_type='c')


class ProviderManager(models.Manager):

    def get_queryset(self):
        return super(ProviderManager, self).get_queryset().filter(company_type='f')


class EmployeeContactManager(models.Manager):

    def get_queryset(self):
        return super(EmployeeContactManager, self).get_queryset().filter(contact_or_phone=True)


class EmployeePhoneManager(models.Manager):

    def get_queryset(self):
        return super(EmployeePhoneManager, self).get_queryset().filter(contact_or_phone=False)
