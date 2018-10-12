from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework import viewsets

from myproject.core.actions import _delete
from .serializers import EmployeeSerializer
from .models import (
    Employee,
    EmployeeBankAccount,
    EmployeeContact,
    EmployeePhone,
    Occupation,
)


def employee_contact(request, pk):
    contacts = EmployeeContact.objects.filter(employee=pk, active=True)
    contacts = contacts.order_by('name')
    data = serializers.serialize('json', contacts)
    return HttpResponse(data, content_type='application/json')


def employee_contact_create(request):
    if request.method == 'POST':
        employee_pk = request.POST['employee']
        employee = Employee.objects.get(pk=employee_pk)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        EmployeeContact.objects.create(
            employee=employee,
            name=name,
            email=email,
            phone=phone
        )
        data = 'OK'
    return HttpResponse(data, content_type='application/json')


def employee_contact_edit(request, pk):
    if request.method == 'POST':
        pk = request.POST['pk']
        employee_contact = EmployeeContact.objects.get(pk=pk)
        employee_contact.name = request.POST['name']
        employee_contact.email = request.POST['email']
        employee_contact.phone = request.POST['phone']
        employee_contact.save()
        contacts = EmployeeContact.objects.filter(
            employee=employee_contact.employee,
            active=True
        )
        contacts = contacts.order_by('name')
        data = serializers.serialize('json', contacts)
    return HttpResponse(data, content_type='application/json')


def employee_phone(request, pk):
    phones = EmployeePhone.objects.filter(employee=pk, active=True)
    data = serializers.serialize('json', phones)
    return HttpResponse(data, content_type='application/json')


def employee_phone_create(request):
    if request.method == 'POST':
        employee_pk = request.POST['employee']
        employee = Employee.objects.get(pk=employee_pk)
        phone = request.POST['phone2']
        phone_type = request.POST['phone_type']
        EmployeePhone.objects.create(
            employee=employee,
            phone=phone,
            phone_type=phone_type,
            contact_or_phone=False,
        )
        data = 'OK'
    return HttpResponse(data, content_type='application/json')


def employee_phone_edit(request, pk):
    if request.method == 'POST':
        pk = request.POST['pk']
        employee_phone = EmployeePhone.objects.get(pk=pk)
        employee_phone.phone = request.POST['phone']
        employee_phone.phone_type = request.POST['phone_type']
        employee_phone.save()
        phones = EmployeePhone.objects.filter(
            employee=employee_phone.employee,
            active=True
        )
        data = serializers.serialize('json', phones)
    return HttpResponse(data, content_type='application/json')


# @login_required()
def employee_phone_delete(request, pk):
    _delete(EmployeePhone, pk)
    return HttpResponseRedirect(reverse_lazy('crm:employee_list'))


def load_phone_types(request):
    ''' Retorna uma lista de tipos de telefones. '''
    pass


# @login_required()
def employee_contact_delete(request, pk):
    _delete(EmployeeContact, pk)
    return HttpResponseRedirect(reverse_lazy('crm:employee_list'))


def load_occupations(request):
    ''' Retorna as Vagas a partir do Departamento escolhido. '''
    department = request.GET.get('department')
    if department:
        occupations = Occupation.objects.filter(department=department)
    else:
        occupations = Occupation.objects.all()
    occupations = occupations.order_by('occupation')
    template_name = 'crm/_include_occupations.html'
    kw = {'occupations': occupations}
    return render(request, template_name, kw)


# @login_required()
def employee_delete(request, pk):
    _delete(Employee, pk)
    return HttpResponseRedirect(reverse_lazy('crm:employee_list'))


def employee_bank(request, pk):
    banks = EmployeeBankAccount.objects.filter(employee=pk, active=True)
    banks = banks.order_by('name')
    data = serializers.serialize('json', banks)
    return HttpResponse(data, content_type='application/json')


def employee_bank_create(request):
    if request.method == 'POST':
        employee_pk = request.POST['employee']
        employee = Employee.objects.get(pk=employee_pk)
        name = request.POST['name']
        bank = request.POST['bank']
        agency = request.POST['agency']
        account = request.POST['account']
        EmployeeBankAccount.objects.create(
            employee=employee,
            name=name,
            bank=bank,
            agency=agency,
            account=account,
        )
        data = 'OK'
    return HttpResponse(data, content_type='application/json')


def employee_bank_edit(request, pk):
    if request.method == 'POST':
        pk = request.POST['pk']
        employee_bank = EmployeeBankAccount.objects.get(pk=pk)
        employee_bank.name = request.POST['bank_name']
        employee_bank.bank = request.POST['bank']
        employee_bank.agency = request.POST['agency']
        employee_bank.account = request.POST['account']
        employee_bank.save()
        banks = EmployeeBankAccount.objects.filter(
            employee=employee_bank.employee,
            active=True
        )
        banks = banks.order_by('name')
        data = serializers.serialize('json', banks)
    return HttpResponse(data, content_type='application/json')


# @login_required()
def employee_bank_delete(request, pk):
    _delete(EmployeeBankAccount, pk)
    return HttpResponseRedirect(reverse_lazy('crm:employee_list'))


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
