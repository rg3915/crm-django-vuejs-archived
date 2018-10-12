import os
import django
import timeit
from datetime import date, datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

import string
import names
from random import choice, randint, random, sample
from django.contrib.auth.models import User, Group, Permission
from django.utils.text import slugify
from myproject.crm.models import (
    Occupation, Employee, Company, Provider, EmployeeBankAccount
)
from myproject.financial.models import TypeExpense, Receipt, Expense
from utils import (
    BANKS,
    COMPANIES,
    EXPENSES,
    LOREM,
    OCCUPATION_LIST,
    PROVIDERS,
    TYPE_EXPENSES,
    USERS,
)


class Utils:
    ''' Métodos genéricos. '''
    @staticmethod
    def gen_string(max_length):
        '''
        Gera uma string randomica.
        '''
        return str(''.join(choice(string.ascii_letters) for i in range(max_length)))
    gen_string.required = ['max_length']

    @staticmethod
    def gen_date(min_year=2018, max_year=datetime.now().year):
        '''
        Gera um date no formato yyyy-mm-dd.
        '''
        start = date(min_year, 1, 1)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        return start + (end - start) * random()

    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))

    def gen_name():
        text = []
        for _ in range(randint(6, 10)):
            text.append(names.get_last_name())
        data = {
            'name': ' '.join(text),
            'social_name': ' '.join(text) + ' Ltda'
        }
        return data

    def gen_text():
        lorem = LOREM.split(' ')
        text = sample(lorem, randint(15, 30))
        return ' '.join(text).title()


class Abstracts:
    '''
    Métodos para retornar dicionários com valores gerados aleatoriamente.
    '''
    @staticmethod
    def abstract_dict(signal_value, title=None):
        if signal_value:
            value = randint(500, 1500) * random()
            _type_expense = TypeExpense.objects.filter(title='Pagamento')
            _type_expense = _type_expense.first()
            type_expense = _type_expense.pk
        else:
            value = -1 * randint(1, 500) * random()
            _type_expense = TypeExpense.objects.get(title=title)
            type_expense = _type_expense.pk
        employee = Employee.objects.all()
        paying_source = choice(employee.values_list('pk', flat=True))
        company = Company.objects.all()
        cost_center = choice(company.values_list('pk', flat=True))
        creator = User.objects.get(email='regis.santos.100@gmail.com')
        return dict(
            payment_date=Utils.gen_date(),
            expiration_date=Utils.gen_date(),
            paying_source_id=paying_source,
            type_expense_id=type_expense,
            cost_center_id=cost_center,
            creator=creator,
            value=value,
            paid=randint(0, 1),
        )


class UserClass:
    '''
    Métodos pra criar User.
    '''

    @staticmethod
    def create_user1(max_itens=None):
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

    @staticmethod
    def create_occupation():
        Occupation.objects.all().delete()
        obj = [Occupation(occupation=val) for val in OCCUPATION_LIST]
        Occupation.objects.bulk_create(obj)

    @staticmethod
    def create_employee():
        for user in USERS:
            _occupation = user.get('occupation')
            occupation = Occupation.objects.get(occupation=_occupation)
            Employee.objects.create(
                username=user['username'],
                email=user['email'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                occupation=occupation,
                city=user['city'],
                uf=user['uf']
            )

    @staticmethod
    def update_pass_of_users():
        for user in USERS:
            _user = User.objects.get(email=user['email'])
            _user.is_staff = True
            _user.is_superuser = True
            _user.set_password('d')
            _user.save()
            if user.get('group_name'):
                group, _ = Group.objects.get_or_create(name=user['group_name'])
                _user.groups.add(group)

    @staticmethod
    def permissions_to_groups():
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
            group = Group.objects.get(name='simpleuser')
            group.permissions.add(permission)
        # Arrumando o grupo de alguns usuarios
        for user in User.objects.filter(groups__name='admin'):
            user.groups.clear()
            group, _ = Group.objects.get_or_create(name='admin')
            user.groups.add(group)

    @staticmethod
    def create_company():
        Company.objects.all().delete()
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

    @staticmethod
    def create_company2(max_itens=20):
        aux = []
        for item in range(max_itens):
            name = Utils.gen_name()['name']
            social_name = Utils.gen_name()['social_name']
            slug = slugify(Utils.gen_name()['name'])
            email = slug + '@email.com'
            address = 'Rua ' + names.get_full_name()
            address_number = randint(100, 9999)
            complement = '14º andar'
            district = 'Centro'
            city = 'São Paulo'
            uf = 'SP'
            cep = Utils.gen_digits(8)
            cnpj = Utils.gen_digits(14)
            ie = Utils.gen_digits(10)
            imun = Utils.gen_digits(10)
            obj = Company(
                name=name,
                social_name=social_name,
                slug=slug,
                email=email,
                address=address,
                address_number=address_number,
                complement=complement,
                district=district,
                city=city,
                uf=uf,
                cep=cep,
                cnpj=cnpj,
                ie=ie,
                imun=imun,
            )
            aux.append(obj)
        Company.objects.bulk_create(aux)

    @staticmethod
    def create_provider():
        Provider.objects.all().delete()
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

    @staticmethod
    def create_bank_account():
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

    @staticmethod
    def create_type_expense():
        TypeExpense.objects.all().delete()
        obj = [TypeExpense(title=val.get('title'), fixed=val.get('fixed'))
               for val in TYPE_EXPENSES]
        TypeExpense.objects.bulk_create(obj)


# class ReceiptClass:

#     @staticmethod
#     def create_receipt(signal_value=True):
#         aux_list = []
#         for i in RECEIPTS:
#             items = Abstracts.abstract_dict(signal_value=signal_value)
#             data = {
#                 'description': i.get('description'),
#                 **items
#             }
#             aux_list.append(Receipt(**data))
#         Receipt.objects.bulk_create(aux_list)


class ExpenseClass:

    @staticmethod
    def create_expense(signal_value=False):
        aux_list = []
        for i in EXPENSES:
            _provider = Provider.objects.all()
            provider = choice(_provider.values_list('pk', flat=True))
            items = Abstracts.abstract_dict(
                signal_value=signal_value,
                title=i.get('type_expense'),
            )
            data = {
                'description': i.get('description'),
                'provider_id': provider,
                **items
            }
            aux_list.append(Expense(**data))
        Expense.objects.bulk_create(aux_list)

    @staticmethod
    def create_expense2(signal_value=False, max_itens=None):
        aux_list = []
        for i in range(max_itens):
            _provider = Provider.objects.all()
            provider = choice(_provider.values_list('pk', flat=True))
            items = Abstracts.abstract_dict(
                signal_value=signal_value,
                title=choice(TYPE_EXPENSES)['title'],
            )
            data = {
                'description': Utils.gen_text(),
                'provider_id': provider,
                **items
            }
            aux_list.append(Expense(**data))
        Expense.objects.bulk_create(aux_list)


tic = timeit.default_timer()

User.objects.all().delete()

UserClass.create_user1()
UserClass.create_occupation()
UserClass.create_employee()
UserClass.update_pass_of_users()
UserClass.permissions_to_groups()
UserClass.create_company()
UserClass.create_company2()
UserClass.create_provider()
UserClass.create_bank_account()
UserClass.create_type_expense()

ExpenseClass.create_expense2(max_itens=200)

toc = timeit.default_timer()
print('time', toc - tic)
