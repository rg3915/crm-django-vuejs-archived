from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from myproject.utils.lists import DEPARTMENT
from .models import Company, Provider, Employee


# class UserAdminCreationForm(UserCreationForm):
# Sem senha definida
class UserAdminCreationForm(forms.ModelForm):
    ''' Cadastro geral de User '''
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.EmailField(label='E-mail', required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']
        # username = email
        self.cleaned_data['username'] = email
        return email

    def save(self, commit=True):
        instance = super(UserAdminCreationForm, self).save(commit=False)
        # Salva username = email
        instance.username = self.cleaned_data['email']
        if commit:
            instance.save()
            # Cria Company
            # create_customer(instance)
        return instance


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = (
            'social_name',
            'name',
            'email',
            'cep',
            'address',
            'address_number',
            'complement',
            'district',
            'city',
            'uf',
        )

    def clean_cep(self):
        return self.cleaned_data['cep'].replace('-', '') if self.cleaned_data['cep'] else self.cleaned_data['cep']

    def clean_cpf(self):
        return self.cleaned_data['cpf'].replace('.', '').replace('-', '') if self.cleaned_data['cpf'] else self.cleaned_data['cpf']

    def clean_cnpj(self):
        return self.cleaned_data['cnpj'].replace('.', '').replace('-', '').replace('/', '') if self.cleaned_data['cnpj'] else self.cleaned_data['cnpj']


class CompanyAdminForm(CompanyForm):

    class Meta:
        model = Company
        fields = CompanyForm.Meta.fields + (
            'cpf',
            'rg',
            'cnh',
            'cnpj',
            'ie',
            'imun',
        )


class ProviderForm(CompanyForm):

    class Meta:
        model = Provider
        fields = CompanyForm.Meta.fields

    def save(self, commit=True):
        instance = super(ProviderForm, self).save(commit=False)
        instance.company_type = 'f'
        if commit:
            instance.save()
        return instance


class PFForm(CompanyForm):
    social_name = forms.CharField(label='Nome')
    name = forms.CharField(label='Sobrenome')

    class Meta:
        model = Company
        fields = CompanyForm.Meta.fields + (
            'cpf',
            'rg',
            'cnh',
        )


class PJForm(CompanyForm):

    class Meta:
        model = Company
        fields = CompanyForm.Meta.fields + (
            'cnpj',
            'ie',
            'imun',
        )


class PFProviderForm(CompanyForm):
    social_name = forms.CharField(label='Nome')
    name = forms.CharField(label='Sobrenome')

    class Meta:
        model = Provider
        fields = CompanyForm.Meta.fields + (
            'cpf',
            'rg',
            'cnh',
        )


class PJProviderForm(CompanyForm):

    class Meta:
        model = Provider
        fields = CompanyForm.Meta.fields + (
            'cnpj',
            'ie',
            'imun',
        )


class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(label='Nome', required=True)
    email = forms.EmailField(label='E-mail', required=True)
    department = forms.ChoiceField(
        choices=[('', '---------')] + [(id[0], id[1]) for id in DEPARTMENT],
        label='Departamento',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Employee
        fields = (
            'first_name',
            'last_name',
            'email',
            'personal_email',
            'birthday',
            'department',
            'occupation',
            'photo',
            'cpf',
            'rg',
            'oab',
            'oab_uf',
            'cep',
            'address',
            'address_number',
            'complement',
            'district',
            'city',
            'uf',
        )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     self.data = self.data.copy()
    #     cpf = self.data.get('cpf')
    #     new_cpf = cpf.replace('.', '').replace('-', '')
    #     self.data['cpf'] = new_cpf

    # def save(self, commit=True):
    #     instance = super(EmployeeForm, self).save(commit=False)
    #     import ipdb
    #     ipdb.set_trace()
    #     if commit:
    #         instance.save()
    #     return instance

    def clean_cep(self):
        return self.cleaned_data['cep'].replace('-', '') if self.cleaned_data['cep'] else self.cleaned_data['cep']

    def clean_cpf(self):
        return self.cleaned_data['cpf'].replace('.', '').replace('-', '') if self.cleaned_data['cpf'] else self.cleaned_data['cpf']


class EmployeeAdminForm(EmployeeForm):

    class Meta():
        model = Employee
        fields = EmployeeForm.Meta.fields + (
            'date_admission',
            'date_release',
            'active',
        )
