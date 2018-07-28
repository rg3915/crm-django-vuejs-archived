from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse, reverse_lazy
from myproject.core.models import TimeStampedModel, Address, Document, Active
from myproject.utils.lists import PHONE_TYPE, PERSON_TYPE, COMPANY_TYPE, DEPARTMENT
from .managers import (
    CompanyManager,
    EmployeeContactManager,
    EmployeePhoneManager,
    PersonManager,
    ProviderManager,
)


def gen_slug(fname, lname, email):
    fullname = '{} {}'.format(fname, lname)
    if fullname.strip():
        slug = slugify(fullname)
    else:
        slug = slugify(email)
    return slug


class People(TimeStampedModel, Address, Document, Active):
    ''' Tabela base de pessoas '''
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    personal_email = models.EmailField('E-mail pessoal', null=True, blank=True)
    slug = models.SlugField()
    photo = models.ImageField('foto', null=True, blank=True)
    birthday = models.DateField('nascimento', null=True, blank=True)
    father = models.CharField(
        'nome do pai',
        max_length=255,
        null=True,
        blank=True
    )
    mother = models.CharField(
        'nome da mãe',
        max_length=255,
        null=True,
        blank=True
    )
    info = models.TextField('informações', null=True, blank=True)

    class Meta:
        abstract = True

    def get_address(self):
        return '{}, {} {}'.format(self.address, self.address_number, self.complement or '')

    def get_address_complement(self):
        return ' - '.join(filter(None, [self.district, self.city, self.uf]))


class Person(People, User):
    person_type = models.CharField(
        'usuário ou funcionário',
        max_length=1,
        choices=PERSON_TYPE,
        default='f'
    )

    objects = PersonManager()

    def get_absolute_url(self):
        pass
        # return r('crm:person_detail', slug=self.slug)


class ContactBase(Active):
    name = models.CharField('Nome', max_length=100, null=True, blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)
    phone = models.CharField('Telefone', max_length=20, null=True, blank=True)
    phone_type = models.CharField(
        'tipo',
        max_length=3,
        choices=PHONE_TYPE,
        default='pri',
    )
    contact_or_phone = models.BooleanField(
        default=True,
        help_text='Contato ou telefone pessoal'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class BankAccountBase(Active):
    name = models.CharField('Nome', max_length=100)
    bank = models.CharField('Banco', max_length=5, null=True, blank=True)
    agency = models.CharField('Agência', max_length=20, null=True, blank=True)
    account = models.CharField('Conta', max_length=20, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '{}-{}-{}'.format(self.bank, self.agency, self.account)


class Company(TimeStampedModel, Address, Document, Active):
    # Razão Social
    social_name = models.CharField('razão social', max_length=100)
    # Nome Fantasia
    name = models.CharField(
        'nome fantasia',
        max_length=100,
        null=True,
        blank=True
    )
    email = models.EmailField(null=True, blank=True)
    slug = models.SlugField()
    info = models.TextField('informações', null=True, blank=True)
    company_type = models.CharField(
        'cliente ou fornecedor',
        max_length=1,
        choices=COMPANY_TYPE,
        default='c'
    )

    objects = CompanyManager()

    class Meta:
        ordering = ('social_name',)
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.social_name

    def get_absolute_url(self):
        return reverse_lazy('crm:company_detail', kwargs={'pk': self.pk})

    def get_address(self):
        return '{}, {} {}'.format(self.address, self.address_number, self.complement or '')

    def get_address_complement(self):
        return ' - '.join(filter(None, [self.district, self.city, self.uf]))

    @property
    def list_url(self):
        return reverse('crm:company_list')

    @property
    def update_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('crm:company_update', kwargs=kw)
        return None

    @property
    def delete_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('crm:company_delete', kwargs=kw)
        return None

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.social_name, self.name, self.email)
        super(Company, self).save(*args, **kwargs)


class CompanyContact(ContactBase):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Contato Empresa'
        verbose_name_plural = 'Contatos Empresas'


class Provider(Company):
    objects = ProviderManager()

    class Meta:
        proxy = True
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'

    def get_absolute_url(self):
        return reverse_lazy('crm:provider_detail', kwargs={'pk': self.pk})

    @property
    def list_url(self):
        return reverse('crm:provider_list')

    @property
    def update_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('crm:provider_update', kwargs=kw)
        return None

    @property
    def delete_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('crm:provider_delete', kwargs=kw)
        return None

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.social_name, self.name, self.email)
        self.company_type = 'f'
        super(Provider, self).save(*args, **kwargs)


class ProviderContact(ContactBase):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Contato Fornecedor'
        verbose_name_plural = 'Contatos Fornecedores'


class Employee(People, User):
    internal = models.BooleanField('interno', default=True)
    occupation = models.ForeignKey(
        'Occupation',
        verbose_name='cargo',
        related_name='employee_occupation',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    date_admission = models.DateTimeField(
        'admissão',
        null=True,
        blank=True
    )
    date_release = models.DateTimeField(
        'saída',
        null=True,
        blank=True
    )
    salary = models.DecimalField(
        'salário',
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('first_name',)
        verbose_name = u'funcionário'
        verbose_name_plural = u'funcionários'

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse_lazy('crm:employee_detail', kwargs={'pk': self.pk})

    full_name = property(__str__)

    def employee_phone_first(self):
        return EmployeePhone.objects.filter(employee=self, active=True, phone_type='pri').first()

    @property
    def list_url(self):
        return reverse('crm:employee_list')

    @property
    def update_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('crm:employee_update', kwargs=kw)
        return None

    @property
    def delete_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('crm:employee_delete', kwargs=kw)
        return None

    def save(self, *args, **kwargs):
        # Salva username = email
        self.username = self.email
        self.slug = gen_slug(self.first_name, self.last_name, self.email)
        super(Employee, self).save(*args, **kwargs)


@receiver(post_save, sender=Employee)
def create_or_update_employee(sender, instance, created, **kwargs):
    if created:
        # Add Group
        simpleuser, _ = Group.objects.get_or_create(name='simpleuser')
        instance.groups.add(simpleuser)


class EmployeeContact(ContactBase):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

    objects = EmployeeContactManager()

    class Meta:
        verbose_name = 'Contato Funcionário'
        verbose_name_plural = 'Contatos Funcionários'


class EmployeePhone(EmployeeContact):
    objects = EmployeePhoneManager()

    class Meta:
        proxy = True
        verbose_name = 'Telefone Funcionário'
        verbose_name_plural = 'Telefones Funcionários'

    def __str__(self):
        return self.phone


class EmployeeBankAccount(BankAccountBase):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Conta do Funcionário'
        verbose_name_plural = 'Contas dos Funcionários'


class Occupation(models.Model):
    occupation = models.CharField('cargo', max_length=50, unique=True)
    department = models.CharField(
        'departamento',
        max_length=3,
        choices=DEPARTMENT,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('occupation',)
        verbose_name = 'cargo'
        verbose_name_plural = 'cargos'

    def __str__(self):
        return self.occupation
