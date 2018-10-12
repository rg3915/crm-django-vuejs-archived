from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from myproject.core.models import TimeStampedModel, Active
from myproject.crm.models import Company, Employee, Provider
# from myproject.storage_backends import PrivateMediaStorage
from .managers import ExpenseManager, ReceiptManager


class Base(TimeStampedModel, Active):
    description = models.CharField('descrição', max_length=500)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField(
        'data de pagto',
        null=True,
        blank=True
    )
    expiration_date = models.DateField(
        'data de vencimento',
        null=True,
        blank=True
    )
    paying_source = models.ForeignKey(
        Employee,
        verbose_name='fonte pagadora',
        related_name='employees',
        on_delete=models.CASCADE
    )
    type_expense = models.ForeignKey(
        'TypeExpense',
        verbose_name='tipo de despesa',
        on_delete=models.CASCADE
    )
    cost_center = models.ForeignKey(
        Company,
        verbose_name='centro de custo',
        related_name='companies',
        help_text='Recebido/Pago ao (cliente)',
        on_delete=models.CASCADE
    )
    provider = models.ForeignKey(
        Provider,
        verbose_name='fornecedor',
        related_name='providers',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    value = models.DecimalField(
        'valor',
        max_digits=9,
        decimal_places=2,
        default=0
    )
    payment = models.BooleanField(
        'Á vista?',
        default=True,
        help_text='Á vista ou Parcelado.'
    )
    paid = models.BooleanField(
        'Pago?',
        default=True,
        help_text='O fornecedor foi pago?'
    )
    cost_center_paid = models.BooleanField(
        'Cliente pagou?',
        default=False,
        help_text='O cliente pagou?'
    )
    payment_cost_center_date = models.DateField(
        'data de pagto do cliente',
        null=True,
        blank=True
    )
    document = models.FileField(
        # storage=PrivateMediaStorage(),
        null=True,
        blank=True
    )
    document_jpg = models.FileField(
        # storage=PrivateMediaStorage(),
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('-payment_date',)

    def __str__(self):
        return self.description

    def to_dict_json_base(self):
        doc_name = ''
        doc_url = ''
        doc_jpg_name = ''
        doc_jpg_url = ''
        if self.document:
            doc_name = self.document.name
            doc_url = self.document.url
        if self.document_jpg:
            doc_jpg_name = self.document_jpg.name
            doc_jpg_url = self.document_jpg.url
        return {
            'pk': self.pk,
            'description': self.description,
            'cost_center': {
                'pk': self.cost_center.pk,
                'name': self.cost_center.social_name,
            },
            'provider': {
                'pk': self.provider.pk if self.provider else '',
                'name': self.provider.social_name if self.provider else '',
            },
            'expiration_date': self.expiration_date,
            'paid': self.paid,
            'cost_center_paid': self.cost_center_paid,
            'paying_source': {
                'pk': self.paying_source.pk,
                'name': self.paying_source.first_name,
            },
            'payment': self.payment,
            'payment_date': self.payment_date,
            'type_expense': {
                'pk': self.type_expense.pk,
                'title': self.type_expense.title,
                'fixed': self.type_expense.fixed,
            },
            'doc': {
                'name': doc_name,
                'url': doc_url,
            },
            'doc_jpg': {
                'name': doc_jpg_name,
                'url': doc_jpg_url,
            },
            'created': self.created,
            'modified': self.modified,
            'active': self.active,
        }

    def _to_dict_json(self):
        data = self.to_dict_json_base()
        return {
            'value': self.value,
            **data
        }


class Expense(Base):
    ''' Despesas '''
    pass

    objects = ExpenseManager()

    '''
    Usage:
    Expense.objects.count()
    Expense.objects.active().count()
    '''

    class Meta:
        proxy = True
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'

    def to_dict_json(self):
        data = self.to_dict_json_base()
        return {
            'value': -1 * self.value,
            **data
        }

    def save(self, *args, **kwargs):
        ''' Despesas é NEGATIVO. '''
        self.value = -1 * abs(self.value)
        super(Expense, self).save(*args, **kwargs)


class Receipt(Base):
    ''' Recebimentos '''
    pass

    objects = ReceiptManager()

    class Meta:
        proxy = True
        verbose_name = 'Recebimento'
        verbose_name_plural = 'Recebimentos'

    def to_dict_json(self):
        data = self.to_dict_json_base()
        return {
            'value': self.value,
            **data
        }

    def save(self, *args, **kwargs):
        ''' Despesas é POSITIVO. '''
        self.value = abs(self.value)
        super(Receipt, self).save(*args, **kwargs)


class TypeExpense(TimeStampedModel, Active):
    ''' Tipo de Despesa '''
    title = models.CharField('título', max_length=70, unique=True)
    fixed = models.BooleanField(
        'fixa',
        default=False,
        help_text='Despesa fixa?'
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Tipo de Despesa'
        verbose_name_plural = 'Tipos de Despesas'

    def __str__(self):
        return self.title

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'title': self.title,
        }


class Repayment(TimeStampedModel, Active):
    '''
    Notas de Reembolso do cliente.
    '''
    creator = models.ForeignKey(
        User,
        related_name='creator',
        on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company,
        related_name='repayment_companies',
        on_delete=models.CASCADE
    )
    expiration_date = models.DateField(
        'data de vencimento',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('pk',)
        verbose_name = 'nota de reembolso'
        verbose_name_plural = 'notas de reembolso'

    def __str__(self):
        return '{} - {}'.format(self.pk, self.company)

    def get_code(self):
        return '{}/{}'.format(str(self.pk).zfill(3), self.created.year)

    def get_total(self):
        qs = self.repayments.filter(
            repayment=self.pk,
            expense__type_expense__fixed=False,
        ).values_list('expense__value', flat=True) or 0
        if qs:
            return sum(qs)
        return 0

    def cost_center_is_paid(self):
        '''
        Verifica se o cliente pagou toda a Nota de Reembolso.
        '''
        is_paid = self.repayments.all()\
            .values_list('expense__cost_center_paid', flat=True)
        if is_paid:
            if list(set(is_paid))[0]:
                return True
        return False

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'company': {
                'pk': self.company.pk,
                'name': self.company.social_name,
            },
            'expiration_date': self.expiration_date,
            'code': self.get_code(),
            'total': -1 * self.get_total(),
            'paid': self.cost_center_is_paid(),
            'url': reverse('financial:repayment_items', kwargs={'pk': self.pk})
        }


class RepaymentItems(TimeStampedModel):
    '''
    Itens das Notas de Reembolso.
    '''
    repayment = models.ForeignKey(
        Repayment,
        related_name='repayments',
        on_delete=models.CASCADE
    )
    expense = models.ForeignKey(
        Expense,
        verbose_name='despesa',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('expense__payment_date',)
        verbose_name = 'item da nota de reembolso'
        verbose_name_plural = 'itens das notas de reembolso'

    def __str__(self):
        if self.repayment:
            return '{} - {}'.format(self.repayment.__str__(), self.expense)
