from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin as PRM
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from myproject.core.actions import _delete
from myproject.core.mixins import ActiveMixin
from .models import (
    Company,
    CompanyContact,
    Employee,
    EmployeeBankAccount,
    EmployeeContact,
    EmployeePhone,
    Occupation,
    Provider,
    ProviderContact,
)
from .forms import (
    CompanyForm,
    EmployeeForm,
    PFForm,
    PFProviderForm,
    PJForm,
    PJProviderForm,
    ProviderForm,
    UserAdminCreationForm,
)
from .mixins import SuccessUrlMixin, ModelName


@login_required()
@permission_required('crm.delete_company')
def company_delete(request, pk):
    _delete(Company, pk)
    return HttpResponseRedirect(reverse_lazy('crm:company_list'))


class CompanyList(ModelName, ActiveMixin, ListView):
    model = Company


class CompanyDetail(ModelName, DetailView):
    model = Company


class CompanyCreate(ModelName, TemplateView):
    model = Company
    template_name = 'crm/company_add.html'


class CompanyUpdate(PRM, ModelName, UpdateView):
    permission_required = 'crm.edit_company'
    model = Company
    form_class = CompanyForm
    template_name = 'crm/company_form.html'
    success_url = reverse_lazy('crm:company_list')


def company_contact(request, pk):
    contacts = CompanyContact.objects.filter(company=pk, active=True)
    contacts = contacts.order_by('name')
    data = serializers.serialize('json', contacts)
    return HttpResponse(data, content_type='application/json')


def company_contact_create(request):
    if request.method == 'POST':
        company_pk = request.POST['company']
        company = Company.objects.get(pk=company_pk)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        CompanyContact.objects.create(
            company=company,
            name=name,
            email=email,
            phone=phone
        )
        data = 'OK'
    return HttpResponse(data, content_type='application/json')


def company_contact_edit(request, pk):
    if request.method == 'POST':
        pk = request.POST['pk']
        company_contact = CompanyContact.objects.get(pk=pk)
        company_contact.name = request.POST['name']
        company_contact.email = request.POST['email']
        company_contact.phone = request.POST['phone']
        company_contact.save()
        # Truque
        # https://stackoverflow.com/a/16640092
        # contact = CompanyContact.objects.filter(pk=pk)
        # Gambiarra - nao e a melhor saida
        contacts = CompanyContact.objects.filter(
            company=company_contact.company,
            active=True
        )
        contacts = contacts.order_by('name')
        data = serializers.serialize('json', contacts)
    return HttpResponse(data, content_type='application/json')


@login_required()
# @permission_required('crm.delete_company_contact')
def company_contact_delete(request, pk):
    _delete(CompanyContact, pk)
    return HttpResponseRedirect(reverse_lazy('crm:company_list'))


class PFRegister(ModelName, CreateView):
    model = Company
    template_name = 'crm/company_form.html'
    form_class = PFForm


class PJRegister(ModelName, CreateView):
    model = Company
    template_name = 'crm/company_form.html'
    form_class = PJForm


@login_required()
@permission_required('crm.delete_provider')
def provider_delete(request, pk):
    _delete(Provider, pk)
    return HttpResponseRedirect(reverse_lazy('crm:provider_list'))


class ProviderList(ModelName, ActiveMixin, ListView):
    model = Provider
    template_name = 'crm/company_list.html'


class ProviderDetail(ModelName, DetailView):
    model = Provider
    template_name = 'crm/company_detail.html'


class ProviderCreate(ModelName, TemplateView):
    model = Provider
    template_name = 'crm/company_add.html'


class ProviderUpdate(PRM, ModelName, UpdateView):
    permission_required = 'crm.edit_provider'
    model = Provider
    form_class = ProviderForm
    template_name = 'crm/company_form.html'
    success_url = reverse_lazy('crm:provider_list')


def provider_contact(request, pk):
    contacts = ProviderContact.objects.filter(provider=pk, active=True)
    contacts = contacts.order_by('name')
    data = serializers.serialize('json', contacts)
    return HttpResponse(data, content_type='application/json')


def provider_contact_create(request):
    if request.method == 'POST':
        provider_pk = request.POST['provider']
        provider = Provider.objects.get(pk=provider_pk)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        ProviderContact.objects.create(
            provider=provider,
            name=name,
            email=email,
            phone=phone
        )
        data = 'OK'
    return HttpResponse(data, content_type='application/json')


def provider_contact_edit(request, pk):
    if request.method == 'POST':
        pk = request.POST['pk']
        provider_contact = ProviderContact.objects.get(pk=pk)
        provider_contact.name = request.POST['name']
        provider_contact.email = request.POST['email']
        provider_contact.phone = request.POST['phone']
        provider_contact.save()
        contacts = ProviderContact.objects.filter(
            provider=provider_contact.provider,
            active=True
        )
        contacts = contacts.order_by('name')
        data = serializers.serialize('json', contacts)
    return HttpResponse(data, content_type='application/json')


@login_required()
# @permission_required('crm.delete_provider_contact')
def provider_contact_delete(request, pk):
    _delete(ProviderContact, pk)
    return HttpResponseRedirect(reverse_lazy('crm:provider_list'))


class PFProvider(ModelName, CreateView):
    model = Provider
    template_name = 'crm/company_form.html'
    form_class = PFProviderForm


class PJProvider(ModelName, CreateView):
    model = Provider
    template_name = 'crm/company_form.html'
    form_class = PJProviderForm


class EmployeeList(ModelName, ActiveMixin, ListView):
    model = Employee


class EmployeeDetail(ModelName, DetailView):
    model = Employee

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetail, self).get_context_data(**kwargs)
        pk = self.object.pk
        email = self.object.email
        token = urlsafe_base64_encode(force_bytes(email)).decode('utf-8')
        # kw = {'uid': uid, 'token': token}
        kw = {'pk': pk, 'token': token}
        current_site = get_current_site(self.request)
        domain = current_site.domain
        return context


class EmployeeDetail2(EmployeeDetail):
    template_name = 'crm/employee_detail2.html'


class EmployeeCreate(ModelName, CreateView):
    model = Employee
    template_name = 'crm/employee_form.html'
    form_class = EmployeeForm


class EmployeeUpdate(PRM, ModelName, UpdateView):
    permission_required = 'crm.edit_employee'
    model = Employee
    form_class = EmployeeForm
    template_name = 'crm/employee_form.html'
    success_url = reverse_lazy('crm:employee_list')


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


@login_required()
# @permission_required('crm.delete_employee_contact')
def employee_phone_delete(request, pk):
    _delete(EmployeePhone, pk)
    return HttpResponseRedirect(reverse_lazy('crm:employee_list'))


def load_phone_types(request):
    ''' Retorna uma lista de tipos de telefones. '''
    pass


@login_required()
# @permission_required('crm.delete_employee_contact')
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


@login_required()
@permission_required('crm.delete_employee')
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


@login_required()
# @permission_required('crm.delete_employee_contact')
def employee_bank_delete(request, pk):
    _delete(EmployeeBankAccount, pk)
    return HttpResponseRedirect(reverse_lazy('crm:employee_list'))
