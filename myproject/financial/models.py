from django.db import models
from myproject.core.models import TimeStampedModel, Active
from myproject.crm.models import Company, Employee


class Expense(TimeStampedModel, Active):
    ''' Despesas '''
    description = models.CharField('descrição', max_length=250)
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
        related_name='employees',
        on_delete=models.CASCADE
    )
    cost_center = models.ForeignKey(
        Company,
        verbose_name='centro de custo',
        related_name='employees',
        help_text='Recebido/Pago ao (cliente)',
        on_delete=models.CASCADE
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
        default=False,
    )

    class Meta:
        ordering = ('-payment_date',)
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'

    def __str__(self):
        return self.description


class Receipt(Expense):
    ''' Recebimentos '''
    pass

    class Meta:
        ordering = ('-payment_date',)
        verbose_name = 'Recebimento'
        verbose_name_plural = 'Recebimentos'


class TypeExpense(TimeStampedModel, Active):
    ''' Tipo de Despesa '''
    title = models.CharField('título', max_length=70, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Tipo de Despesa'
        verbose_name_plural = 'Tipos de Despesas'

    def __str__(self):
        return self.title
