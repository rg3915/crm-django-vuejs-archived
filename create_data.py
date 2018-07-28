import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from random import choice, randint
from django.contrib.auth.models import User, Group, Permission
from decouple import config
from myproject.crm.models import Occupation, Employee, Company, Provider, EmployeeBankAccount
from myproject.financial.models import TypeExpense


User.objects.all().delete()

user = User.objects.create_user(
    username='admin',
    email='admin@email.com',
    first_name='Admin',
    last_name='Regis',
    is_staff=True,
    is_superuser=True,
)
user.set_password('d')
user.save()


USERS = [
    {
        'username': 'regis@email.com',
        'email': 'regis@email.com',
        'first_name': 'Regis',
        'last_name': 'Email',
        'group_name': 'admin',
        'occupation': 'Desenvolvedor',
        'city': 'São Paulo',
        'uf': 'SP'
    },
]

my_debug = False

if my_debug:
    password = config('PASSWORD')
else:
    password = 'd'


OCCUPATION_LIST = (
    'Analista de sistemas',
    'Backend',
    'DBA',
    'Desenvolvedor',
    'Frontend',
    'Programador',
    'Suporte',
)

Occupation.objects.all().delete()

obj = [Occupation(occupation=val) for val in OCCUPATION_LIST]
Occupation.objects.bulk_create(obj)


# Criando funcionarios
for user in USERS:
    occupation = Occupation.objects.get(occupation=user.get('occupation'))
    Employee.objects.create(
        username=user['username'],
        email=user['email'],
        first_name=user['first_name'],
        last_name=user['last_name'],
        occupation=occupation,
        city=user['city'],
        uf=user['uf']
    )

# Criando usuarios
for user in USERS:
    _user = User.objects.get(email=user['email'])
    _user.is_staff = True
    _user.is_superuser = True
    _user.set_password('d')
    _user.save()
    if user.get('group_name'):
        group, _ = Group.objects.get_or_create(name=user['group_name'])
        _user.groups.add(group)

# Dando permissão ao grupo
permissions = (
    'change_company',
    'change_provider',
    'delete_provider',
    'change_employee',
    'delete_employee',
)
for codename in permissions:
    permission = Permission.objects.get(codename=codename)
    group.permissions.add(permission)

# Arrumando o grupo de alguns usuarios
for user in User.objects.filter(groups__name='admin'):
    user.groups.clear()
    group, _ = Group.objects.get_or_create(name='admin')
    user.groups.add(group)


# Criando 3 clientes
COMPANIES = [
    {
        'name': 'Fernando',
        'social_name': 'Silva',
        'email': 'fernando@email.com',
        'slug': 'fernando-silva',
        'address': 'Rua da Consolação',
        'address_number': '1000',
        'complement': '',
        'district': 'Bela Vista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01302001',
        'cpf': '26696093095',
        'rg': '480728793',
        'cnh': '26405738956',
    },
    {
        'name': 'Accenture',
        'social_name': 'Accenture SA',
        'email': 'accenture@email.com',
        'slug': 'accenture',
        'address': 'Av. Brasil',
        'address_number': '4500',
        'complement': '',
        'district': 'Jardim Paulista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01400100',
        'cnpj': '63895690000104',
        'ie': '362012167511',
        'imun': '603103924168',
    },
    {
        'name': 'Bosch',
        'social_name': 'Bosch SA',
        'email': 'bosch@email.com',
        'slug': 'bosch',
        'address': 'Av. Paulista',
        'address_number': '2200',
        'complement': '5 andar',
        'district': 'Bela Vista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01310000',
        'cnpj': '61905039000142',
        'ie': '860233791246',
        'imun': '522291369401',
    },
]

for company in COMPANIES:
    Company.objects.create(
        name=company.get('name'),
        social_name=company.get('social_name'),
        email=company.get('email'),
        slug=company.get('slug'),
        address=company.get('address'),
        address_number=company.get('address_number'),
        complement=company.get('complement'),
        district=company.get('district'),
        city=company.get('city'),
        uf=company.get('uf'),
        cep=company.get('cep'),
        cpf=company.get('cpf'),
        rg=company.get('rg'),
        cnh=company.get('cnh'),
        cnpj=company.get('cnpj'),
        ie=company.get('ie'),
        imun=company.get('imun'),
    )


# Criando 2 fornecedores
PROVIDERS = [
    {
        'name': 'Atlassian',
        'social_name': 'Atlassian SA',
        'email': 'atlassian@email.com',
        'slug': 'atlassian',
        'address': 'Av. Paulista',
        'address_number': '1000',
        'complement': '',
        'district': 'Bela Vista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01310001',
        'cnpj': '61905039000150',
        'ie': '860233791250',
        'imun': '522291369503',
    },
    {
        'name': 'Heroku',
        'social_name': 'Heroku SA',
        'email': 'heroku@email.com',
        'slug': 'heroku',
        'address': 'Av. Paulista',
        'address_number': '1',
        'complement': '',
        'district': 'Bela Vista',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01311000',
        'cnpj': '61905039000120',
        'ie': '860233791200',
        'imun': '522291369000',
    },
]

for provider in PROVIDERS:
    Provider.objects.create(
        name=provider.get('name'),
        social_name=provider.get('social_name'),
        email=provider.get('email'),
        slug=provider.get('slug'),
        address=provider.get('address'),
        address_number=provider.get('address_number'),
        complement=provider.get('complement'),
        district=provider.get('district'),
        city=provider.get('city'),
        uf=provider.get('uf'),
        cep=provider.get('cep'),
        cpf=provider.get('cpf'),
        rg=provider.get('rg'),
        cnh=provider.get('cnh'),
        cnpj=provider.get('cnpj'),
        ie=provider.get('ie'),
        imun=provider.get('imun'),
    )


# Criando contas bancarias
BANKS = [
    {
        'name': 'Banco do Brasil',
        'bank': '001',
    },
    {
        'name': 'Bradesco',
        'bank': '237',
    },
    {
        'name': 'Itaú',
        'bank': '341',
    },
    {
        'name': 'Santander',
        'bank': '033',
    }
]

for employee in Employee.objects.all():
    for _ in range(3):
        bank = choice(BANKS)
        agency = randint(1000, 9999)
        account = randint(100000, 999999)
        EmployeeBankAccount.objects.create(
            employee=employee,
            name=bank['name'],
            bank=bank['bank'],
            agency=agency,
            account=account,
        )


# Criando Tipo de Despesas
TYPE_EXPENSES = (
    {
        'title': 'Agua'
    },
    {
        'title': 'Almoço'
    },
    {
        'title': 'Aluguel'
    },
    {
        'title': 'Cartório'
    },
    {
        'title': 'Internet'
    },
    {
        'title': 'Luz'
    },
    {
        'title': 'Motoboy'
    },
    {
        'title': 'Viagem'
    },
)

obj = [TypeExpense(title=val['title']) for val in TYPE_EXPENSES]
TypeExpense.objects.bulk_create(obj)
